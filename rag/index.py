from dotenv import load_dotenv
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

# PDF path
pdf_path = Path(__file__).parent / "Nodejs.pdf"

# Load PDF
loader = PyPDFLoader(str(pdf_path))
docs = loader.load()

# Split into chunks (RAG-optimized)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)
chunks = text_splitter.split_documents(docs)

# HuggingFace Embeddings (NO API KEY REQUIRED)
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Store in Qdrant
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag",
    force_recreate=True
)
print(" Indexing completed successfully using HuggingFace embeddings")