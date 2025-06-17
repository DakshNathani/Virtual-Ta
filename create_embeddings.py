import os
import numpy as np
import time
from openai import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

# --- Configuration ---
# 1. Directory containing the markdown files
CONTENT_DIRECTORY = "content"

# 2. Text splitting parameters
CHUNK_SIZE = 1000  # Max characters per chunk
CHUNK_OVERLAP = 150 # Characters to overlap between chunks

# 3. OpenAI Embedding model
# text-embedding-3-small is a powerful and cost-effective new model.
MODEL_NAME = "text-embedding-3-small" 

# 4. API call batch size (OpenAI API has limits on tokens per request)
# 2048 is a safe batch size for this model.
BATCH_SIZE = 1000

# 5. Output file for the compressed NumPy data
OUTPUT_FILE = "embeddings_openai.npz"

# --- Important Note on Cost ---
# Running this script will make API calls to OpenAI, which will incur costs.
# Please monitor your usage and costs in your OpenAI account dashboard.
# For the number of files you have, the cost should be very low (likely a few cents).

# --- Main Script ---

def find_markdown_files(root_dir):
    """Finds all markdown files in a directory and its subdirectories."""
    md_files = []
    print(f"Searching for .md files in '{root_dir}'...")
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(".md"):
                md_files.append(os.path.join(dirpath, filename))
    print(f"Found {len(md_files)} markdown files.")
    return md_files

def create_chunks(file_list):
    """Reads files and splits their content into chunks with metadata."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
    )
    
    all_chunks = []
    source_files = []
    
    for i, file_path in enumerate(file_list):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if not content.strip():
                print(f"  - Skipping empty file: {file_path}")
                continue

            base_name = os.path.basename(file_path)
            chunks = text_splitter.split_text(content)
            if base_name != 'all_discourse_topics.md':
                for i in range(len(chunks)):
                    chunks[i] += '\nWebsite - https://tds.s-anand.net/#/{}'.format(base_name)
            all_chunks.extend(chunks)
            source_files.extend([file_path] * len(chunks))
            
            print(f"  ({i+1}/{len(file_list)}) Processed '{file_path}', created {len(chunks)} chunks.")

        except Exception as e:
            print(f"  - Error processing file {file_path}: {e}")
            
    return all_chunks, source_files

def generate_openai_embeddings(chunks, model_name):
    """Generates embeddings for a list of text chunks using OpenAI's API."""
    print("\nInitializing OpenAI client...")
    try:
        # The client automatically looks for the OPENAI_API_KEY environment variable.
        client = OpenAI(
            api_key = "OPENAI_API_KEY",  # Ensure this environment variable is set
            base_url="https://aipipe.org/openai/v1"
            )
        # A quick check to see if the key is present
        if not client.api_key:
            raise ValueError("OPENAI_API_KEY environment variable not found.")
    except Exception as e:
        print(f"Error initializing OpenAI client: {e}")
        print("Please make sure you have set the OPENAI_API_KEY environment variable.")
        return None

    print(f"Generating embeddings for {len(chunks)} chunks using '{model_name}'...")
    start_time = time.time()
    
    all_embeddings = []
    
    # Process chunks in batches to be efficient and avoid API rate limits
    for i in range(0, len(chunks), BATCH_SIZE):
        batch = chunks[i:i + BATCH_SIZE]
        
        try:
            print(f"  - Processing batch {i//BATCH_SIZE + 1}/{(len(chunks)-1)//BATCH_SIZE + 1}...")
            response = client.embeddings.create(
                model=model_name,
                input=batch
            )
            # Extract the embedding vectors from the API response
            batch_embeddings = [item.embedding for item in response.data]
            all_embeddings.extend(batch_embeddings)
            
        except Exception as e:
            print(f"    !! An error occurred during API call for batch {i}: {e}")
            print("    !! Skipping this batch.")
            # Add placeholders (e.g., None) for the failed batch to maintain index integrity
            all_embeddings.extend([None] * len(batch))

    end_time = time.time()
    print(f"Embedding generation completed in {end_time - start_time:.2f} seconds.")
    
    # Filter out any 'None' entries from failed API calls before converting to numpy array
    successful_embeddings = [emb for emb in all_embeddings if emb is not None]
    if not successful_embeddings:
        print("No embeddings were successfully generated.")
        return None

    return np.array(successful_embeddings)

if __name__ == "__main__":
    markdown_files = find_markdown_files(CONTENT_DIRECTORY)

    if not markdown_files:
        print("No markdown files found. Exiting.")
    else:
        print("\nCreating text chunks...")
        text_chunks, source_metadata = create_chunks(markdown_files)

        if not text_chunks:
            print("No text content found to embed. Exiting.")
        else:
            embedding_vectors = generate_openai_embeddings(text_chunks, MODEL_NAME)

            if embedding_vectors is not None:
                print(f"\nSaving data to '{OUTPUT_FILE}'...")
                np.savez_compressed(
                    OUTPUT_FILE,
                    embeddings=embedding_vectors,
                    chunks=np.array(text_chunks, dtype=object),
                    sources=np.array(source_metadata, dtype=object)
                )
                print("---")
                print("✅ Process complete!")
                print(f"Total chunks created: {len(text_chunks)}")
                print(f"Shape of embeddings array: {embedding_vectors.shape}")
                print(f"Data saved successfully to {OUTPUT_FILE}")
                print("---\n")
                
                # Verify the saved file
                print("Verifying saved file...")
                loaded_data = np.load(OUTPUT_FILE, allow_pickle=True)
                print(f"Loaded keys: {list(loaded_data.keys())}")
                print(f"First chunk source: {loaded_data['sources'][0]}")
                print(f"First chunk text: '{loaded_data['chunks'][0][:100]}...'")
