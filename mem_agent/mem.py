from google import genai
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, VectorParams, Distance
from dotenv import load_dotenv
import os
import uuid

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
qdrant = QdrantClient("localhost", port=6333)

COLLECTION_NAME = "chat_memory"
EMBEDDING_MODEL = "gemini-embedding-001"
CHAT_MODEL = "gemini-2.5-flash"
VECTOR_SIZE = 3072

# ✅ Safe collection initialization (recreate_collection is deprecated)
existing = [c.name for c in qdrant.get_collections().collections]
if COLLECTION_NAME in existing:
    qdrant.delete_collection(COLLECTION_NAME)

qdrant.create_collection(
    collection_name=COLLECTION_NAME,
    vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE)
)

print("Chat started. Type 'exit' to quit.\n")

while True:
    user_query = input("You: ").strip()

    if user_query.lower() in ("exit", "quit"):
        print("Goodbye!")
        break

    if not user_query:
        continue

    # ✅ Single embedding call, reused for both search and storage
    embedding_response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=user_query
    )
    query_vector = embedding_response.embeddings[0].values

    # Retrieve relevant memories
    search_result = qdrant.query_points(
        collection_name=COLLECTION_NAME,
        query=query_vector,
        limit=3
    )

    # ✅ Build memory context string to inject into the prompt
    memory_context = ""
    if search_result.points:
        memory_lines = []
        for hit in search_result.points:
            memory_lines.append(
                f"  User: {hit.payload['user']}\n  Assistant: {hit.payload['assistant']}"
            )
        memory_context = "Relevant past exchanges:\n" + "\n\n".join(memory_lines) + "\n\n"
        print("\n[Memory Retrieved]")
        for hit in search_result.points:
            print(f"  - {hit.payload['user'][:60]}...")

    # ✅ Inject memories into the prompt
    full_prompt = f"{memory_context}Current user message: {user_query}"

    response = client.models.generate_content(
        model=CHAT_MODEL,
        contents=full_prompt
    )

    ai_response = response.text
    print(f"\nAI: {ai_response}")

    # Store this exchange in Qdrant
    qdrant.upsert(
        collection_name=COLLECTION_NAME,
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=query_vector,  # ✅ Reuse existing vector
                payload={
                    "user": user_query,
                    "assistant": ai_response
                }
            )
        ]
    )
