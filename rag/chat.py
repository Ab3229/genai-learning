from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

# Embedding model (local, no API key)
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Connect to existing Qdrant collection
vector_store = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

# User query
user_query = input("Ask anything: ")

# Retrieve top 3 chunks
search_result = vector_store.similarity_search(
    query=user_query,
    k=3
)

# Build context
context = "\n\n".join(
    [
        f"Page {doc.metadata.get('page', 'N/A')}:\n{doc.page_content}"
        for doc in search_result
    ]
)

# Prompt
final_prompt = f"""
You are a helpful AI assistant.
Answer ONLY from the given context.
If the answer is not present, say: Information not found in document.

Context:
{context}

Question:
{user_query}
"""

# Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=final_prompt
)

print(response.text)