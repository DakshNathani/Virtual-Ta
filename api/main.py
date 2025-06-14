# api/main.py

import os
import numpy as np
import openai
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from typing import List, Optional
import json
import logging
from dotenv import load_dotenv
from contextlib import asynccontextmanager

# Load environment variables (for local testing, this path is still correct)
load_dotenv(dotenv_path="../.env")

# --- Configuration & Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# --- FINAL ROBUST PATHING LOGIC ---
# Get the directory where this script (main.py) is located.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Construct the absolute path to the embeddings file, which is in the SAME directory.
EMBEDDINGS_FILE = os.path.join(SCRIPT_DIR, "embeddings_openai.npz")
# --- END OF FIX ---


if "OPENAI_API_KEY" not in os.environ:
    logger.warning("OPENAI_API_KEY environment variable not set.")
if "OPENAI_BASE_URL" not in os.environ:
    logger.warning("OPENAI_BASE_URL environment variable not set. Using default OpenAI API.")

client = openai.OpenAI()
knowledge_base = {}


# --- OPTIMIZATION: REPLACEMENT FOR SCIKIT-LEARN ---
def cosine_similarity_numpy(vec1, vec2_matrix):
    """Calculates cosine similarity between a vector and a matrix of vectors using only numpy."""
    # Ensure vec1 is a 2D array
    if vec1.ndim == 1:
        vec1 = vec1.reshape(1, -1)
        
    dot_product = np.dot(vec2_matrix, vec1.T).flatten()
    
    # Calculate norms and add a small epsilon for numerical stability
    norms = np.linalg.norm(vec2_matrix, axis=1) * np.linalg.norm(vec1) + 1e-8
    
    similarities = dot_product / norms
    return similarities
# --- END OF OPTIMIZATION ---


@asynccontextmanager
async def lifespan(app: FastAPI):
    # This code runs on startup
    global knowledge_base
    try:
        if os.path.exists(EMBEDDINGS_FILE):
            logger.info(f"Loading knowledge base from {EMBEDDINGS_FILE}...")
            data = np.load(EMBEDDINGS_FILE, allow_pickle=True)
            knowledge_base = {
                "embeddings": data["embeddings"],
                "chunks": data["chunks"],
                "sources": data["sources"]
            }
            logger.info("Knowledge base loaded successfully.")
            logger.info(f"Loaded {len(knowledge_base['chunks'])} chunks.")
        else:
            logger.error(f"{EMBEDDINGS_FILE} not found. RAG will not work.")
            knowledge_base = {}
    except Exception as e:
        logger.error(f"Failed to load knowledge base: {e}")
        knowledge_base = {}
    
    yield  # The application runs while the 'yield' is active
    
    logger.info("Application shutting down.")


# Pydantic Models
class APIRequest(BaseModel):
    question: str
    image: Optional[str] = None

class Link(BaseModel):
    url: str
    text: str

class APIResponse(BaseModel):
    answer: str
    links: List[Link]


# FastAPI Application Setup
app = FastAPI(lifespan=lifespan)

def get_image_description(base64_image: str) -> str:
    logger.info("Getting image description from vision model...")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Describe this image for a virtual teaching assistant. Focus on any text, code, or user interface elements. This description will be used to answer a student's question."},
                        {"type": "image_url", "image_url": {"url": f"data:image/webp;base64,{base64_image}"}},
                    ],
                }
            ],
            max_tokens=300,
        )
        description = response.choices[0].message.content
        logger.info(f"Image description received: {description[:100]}...")
        return description
    except Exception as e:
        logger.error(f"Error getting image description: {e}")
        return "Could not analyze the image."


def retrieve_context(query: str, top_k: int = 5):
    if not knowledge_base or "embeddings" not in knowledge_base:
        logger.warning("Knowledge base is empty. Skipping retrieval.")
        return "No context available. The knowledge base is not loaded.", []
    logger.info(f"Retrieving context for query: {query[:100]}...")
    query_embedding_response = client.embeddings.create(
        input=[query],
        model="text-embedding-3-small"
    )
    query_embedding = np.array(query_embedding_response.data[0].embedding).reshape(1, -1)
    
    # Use the new numpy-based similarity function
    similarities = cosine_similarity_numpy(query_embedding, knowledge_base["embeddings"])

    top_k_indices = similarities.argsort()[-top_k:][::-1]
    context = ""
    sources = set()
    for i in top_k_indices:
        source_file = knowledge_base['sources'][i]
        chunk_text = knowledge_base['chunks'][i]
        context += f"[Source: {source_file}]\n{chunk_text}\n\n"
        sources.add(f"file:///{source_file}")
    logger.info(f"Retrieved {len(top_k_indices)} context chunks.")
    return context, list(sources)


@app.post("/api/", response_model=APIResponse)
async def process_query(request: APIRequest):
    logger.info(f"Received question: {request.question}")
    full_question = request.question
    if request.image:
        logger.info("Image data found, processing...")
        image_description = get_image_description(request.image)
        full_question = f"User's question: '{request.question}'\n\nContext from attached image: '{image_description}'"
    context, source_links = retrieve_context(full_question)
    system_prompt = """
    You are a helpful and precise virtual teaching assistant for 'The Data Storyteller' course.
    Your task is to answer the user's question based *only* on the provided context.
    Do not use any external knowledge. If the context does not contain the answer,
    state that you cannot answer the question with the available information.

    Your response MUST be a JSON object with two keys: "answer" and "links".
    - "answer": A helpful, concise string that directly answers the user's question based on the context.
    - "links": A list of JSON objects. Each object should have a "url" and a "text" key.
      You MUST find real URLs (e.g., from discourse.onlinedegree.iitm.ac.in) if they are present in the context.
      If no real URLs are in the context, create a link object using the file path provided in the [Source: ...] tag and a descriptive text.
    """
    user_prompt = f"""
    --- CONTEXT ---
    {context}
    --- QUESTION ---
    {request.question}

    --- YOUR JSON RESPONSE ---
    """
    logger.info("Generating final answer with LLM...")
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            response_format={"type": "json_object"}
        )
        final_response_json = response.choices[0].message.content
        logger.info(f"LLM JSON response received: {final_response_json}")
        response_data = json.loads(final_response_json)
        return APIResponse(**response_data)
    except Exception as e:
        logger.error(f"Error during final LLM call or response parsing: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate a response from the AI model.")


@app.get("/")
def read_root():
    return {"status": "ok", "knowledge_base_loaded": "embeddings" in knowledge_base}
