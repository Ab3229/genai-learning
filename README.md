# genai-learning
A Generative AI learning and experimentation repository covering tokenization, LLM agents, RAG pipelines, memory systems, APIs, and a real-time AI voice assistant built with Python and Gemini.

## Repository Overview

This repository contains multiple experiments and implementations related to Generative AI:

### 1. Fundamentals
- **01_tokenization**  
  Understanding tokenization and how text is converted into tokens for LLM processing.

- **hf_basic**  
  Basic experiments with HuggingFace models and transformers.

- **hello_world**  
  Initial experiments with simple LLM interactions.

---

### 2. AI Agents
- **agent_adk**  
  Experiments with building AI agents and orchestration systems.

- **langgraph_learning**  
  Learning LangGraph for building structured AI workflows.

---

### 3. Memory Systems
- **mem_agent**  
  Implementation of memory systems for AI agents to maintain conversational context.

---

### 4. Retrieval Augmented Generation (RAG)
- **rag**  
  Basic implementation of RAG pipelines.

- **rag_queue**  
  Advanced experimentation with retrieval pipelines and query management.

---

### 5. Backend & Local Model APIs
- **ollama_fastapi**  
  Running local models and exposing them through FastAPI endpoints.

---

### 6. Prompt Engineering
- **prompts**  
  Experiments with prompt design and optimization.

---

### 7. AI Applications
- **voice_agent**  
  A real-time AI voice assistant that:
  - Accepts voice input
  - Converts speech to text
  - Generates responses using a Generative AI model
  - Converts the response back to speech

- **wheather**  
  Simple AI-based weather query application.

- **image**  
  Experiments related to image processing or generation.

---

## Tech Stack

- Python
- Google Gemini API
- SpeechRecognition
- gTTS (Google Text-to-Speech)
- LangGraph
- HuggingFace Transformers
- FastAPI
- Vector Databases
- RAG Architectures

---

## Example Interaction

User asks:

"Who is the Prime Minister of India?"

The system processes the speech input, sends the query to the AI model, and responds:

"The Prime Minister of India is Narendra Modi."

---
## 🎥 Project Demo Video

Watch the working demo of the **AI Voice Assistant** here:

🔗 [Watch the Demo Video](https://drive.google.com/file/d/15PpuXxQlNF6CO4ZbVZXsFo5ewJASth4c/view?usp=drive_link)

The video demonstrates:
- Voice input processing
- Speech-to-text conversion
- AI response generation using Gemini
- Text-to-speech output
