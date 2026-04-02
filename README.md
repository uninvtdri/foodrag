# Food RAG - Cloud Migration

A cloud-powered Food RAG (Retrieval-Augmented Generation) system migrated from local ChromaDB and Ollama to Upstash Vector and Groq Cloud.

## Live Demo
https://v0-food-rag-app-04.vercel.app

## Architecture

### Local Version (Week 2)
- Vector DB: ChromaDB (local)
- Embeddings: Ollama (mxbai-embed-large)
- LLM: Ollama (llama3.2)
- Interface: Python CLI

### Cloud Version (Week 3)
- Vector DB: Upstash Vector (cloud)
- Embeddings: Upstash built-in (BGE_SMALL_EN_V1_5)
- LLM: Groq Cloud (llama-3.1-8b-instant)
- Interface: Next.js Web App on Vercel

## Repository Structure

foodrag/
- local-version/ : Original Week 2 ChromaDB system
- cloud-version/ : New Upstash and Groq implementation
- data/ : Enhanced food database with 90 items
- docs/ : Migration plan and documentation
- app/ : Next.js web application
- lib/ : RAG pipeline code

## Environment Variables

UPSTASH_VECTOR_REST_URL - Your Upstash Vector database URL
UPSTASH_VECTOR_REST_TOKEN - Your Upstash Vector authentication token
GROQ_API_KEY - Your Groq Cloud API key

## Setup Instructions

### Local Version
pip install chromadb ollama
python3 rag_run.py

### Cloud Version
pip install upstash-vector groq python-dotenv
python3 migrate_data.py
npm install
npm run dev

## Local vs Cloud Comparison

Feature         | Local Version      | Cloud Version
----------------|--------------------|------------------
Vector DB       | ChromaDB           | Upstash Vector
Embeddings      | Ollama             | Upstash built-in
LLM             | Ollama llama3.2    | Groq llama-3.1-8b
Interface       | Python CLI         | Next.js Web App
Deployment      | Local only         | Vercel (global)
Response Time   | 3-5 seconds        | Under 1 second
Cost            | Free (local)       | Free tier

## Food Database

The database contains 90 diverse food items including:
- Filipino cuisine: Sinigang, Adobo, Bulalo, Caldereta
- Asian cuisine: Pad Thai, Ramen, Kimchi, Bibimbap
- Mediterranean: Hummus, Baklava, Falafel, Tabbouleh
- Health foods: Oatmeal, Quinoa, Tofu, Steamed fish
- Comfort foods: Mac and cheese, Lasagna, Poutine

## Test Queries

1. What is sinigang?
2. Tell me about healthy foods
3. What Filipino foods do you know?
4. What are some spicy dishes?
5. Tell me about Japanese food
6. What are good vegetarian options?
7. Tell me about Korean cuisine
8. What is a good high protein food?
9. Tell me about Mediterranean food
10. What are some comfort foods?
11. What Thai dishes do you know?
12. Tell me about desserts
13. What are some Asian soups?
14. Tell me about street food
15. What are some Indonesian dishes?

## Version History

v1.0 - Local ChromaDB and Ollama system
v2.0 - Cloud Upstash and Groq migration with Next.js web interface
