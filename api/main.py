# api/main.py

import os
import numpy as np
import openai
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from typing import List, Optional
from sklearn.metrics.pairwise import cosine_similarity
import json
import logging
from dotenv import load_dotenv
from contextlib import asynccontextmanager # <-- ADD THIS

# Load environment variables from .env file in the parent directory
load_dotenv(dotenv_path="../.env")

# --- Configuration & Logging ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if "OPENAI_API_KEY" not in os.environ:
    logger.warning("OPENAI_API_KEY environment variable not set.")
if "OPENAI_BASE_URL" not in os.environ:
    logger.warning("OPENAI_BASE_URL environment variable not set. Using default OpenAI API.")

client = openai.OpenAI()

# --- CHANGE 1: Corrected path for embeddings file ---
EMBEDDINGS_FILE = "../embeddings_openai.npz"
knowledge_base = {}

# --- CHANGE 2: Using the modern 'lifespan' event handler ---
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
    
    # This code runs on shutdown (optional)
    logger.info("Application shutting down.")


# --- Pydantic Models ---
class APIRequest(BaseModel):
    question: str
    image: Optional[str] = None

class Link(BaseModel):
    url: str
    text: str

class APIResponse(BaseModel):
    answer: str
    links: List[Link]


# --- FastAPI Application Setup ---
# --- CHANGE 3: Pass the lifespan manager to the app ---
app = FastAPI(lifespan=lifespan)

# THE OLD @app.on_event("startup") FUNCTION HAS BEEN REMOVED

def get_image_description(base64_image: str) -> str:
    # ... (rest of your code remains exactly the same)
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
    # ... (rest of your code remains exactly the same)
    if not knowledge_base or "embeddings" not in knowledge_base:
        logger.warning("Knowledge base is empty. Skipping retrieval.")
        return "No context available. The knowledge base is not loaded.", []
    logger.info(f"Retrieving context for query: {query[:100]}...")
    query_embedding_response = client.embeddings.create(
        input=[query],
        model="text-embedding-3-small"
    )
    query_embedding = np.array(query_embedding_response.data[0].embedding).reshape(1, -1)
    similarities = cosine_similarity(query_embedding, knowledge_base["embeddings"])[0]
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
    # ... (rest of your code remains exactly the same)
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