# Food RAG - Full Stack AI Web Application

A production-ready Food RAG (Retrieval-Augmented Generation) web application built with Next.js, Upstash Vector, and Groq Cloud. This project documents the complete development journey from a local Python CLI to a modern web application.

## Live Demo
https://v0-food-rag-app-04.vercel.app

## GitHub Repository
https://github.com/uninvtdri/foodrag

## Development Journey

Week 2 - Local Python CLI using ChromaDB and Ollama
Week 3 - Cloud migration using Upstash Vector and Groq API
Week 4 - Full stack web application using Next.js deployed on Vercel

## Technology Stack

Frontend: Next.js 15, React 19, Tailwind CSS
Backend: Next.js Server Actions
Vector Database: Upstash Vector with BGE_SMALL_EN_V1_5 embeddings
LLM: Groq Cloud llama-3.1-8b-instant
Deployment: Vercel
AI Development Tool: v0.dev

## Architecture

User sends question via web interface
Next.js Server Action receives the question
Upstash Vector performs semantic search across 90 food items
Top 5 relevant results are retrieved as context
Groq LLM generates a response using the context
Sources and AI response are displayed to the user

## Repository Structure

foodrag/
- app/ : Next.js web application
- lib/ : RAG pipeline with Upstash Vector and Groq
- python-reference/ : Original Python CLI code for comparison
- local-version/ : Week 2 ChromaDB local system
- cloud-version/ : Week 3 Upstash cloud system
- data/ : Enhanced food database with 90 items
- docs/ : Migration plan, performance comparison, test results

## Environment Variables

UPSTASH_VECTOR_REST_URL - Upstash Vector database URL
UPSTASH_VECTOR_REST_TOKEN - Upstash Vector authentication token
GROQ_API_KEY - Groq Cloud API key

## Setup Instructions

### Run locally
git clone https://github.com/uninvtdri/foodrag
cd foodrag
npm install
npm run dev

### Upload food data to Upstash
pip install upstash-vector python-dotenv
python3 migrate_data.py

## Food Database

90 diverse food items including:
- Filipino cuisine: Sinigang, Adobo, Bulalo, Caldereta, Igado
- Asian cuisine: Pad Thai, Ramen, Kimchi, Bibimbap, Pho
- Mediterranean: Hummus, Baklava, Falafel, Tabbouleh, Shawarma
- Health foods: Oatmeal, Quinoa, Tofu, Steamed fish, Boiled egg
- Comfort foods: Mac and cheese, Lasagna, Hamburger, Croissant
- Street food: Tacos, Dim sum, Tteokbokki, Momo, Spam musubi

## Performance Metrics

Local System (Week 2):
- Response time: 3 to 5 seconds
- Requires local machine with Ollama installed
- No internet access needed

Cloud System (Week 3 and 4):
- Response time: under 1 second
- Accessible from any device worldwide
- No local dependencies required

## Local vs Cloud Comparison

Feature         | Local Version      | Cloud Version
----------------|--------------------|------------------
Vector DB       | ChromaDB           | Upstash Vector
Embeddings      | Ollama             | Upstash built-in
LLM             | Ollama llama3.2    | Groq llama-3.1-8b
Interface       | Python CLI         | Next.js Web App
Deployment      | Local only         | Vercel global
Response Time   | 3 to 5 seconds     | Under 1 second
Cost            | Free local         | Free tier

## Test Queries

The system was tested with 15 diverse queries including:
- What is sinigang?
- Tell me about healthy foods
- What Filipino foods do you know?
- What are some spicy dishes?
- Tell me about Japanese food
- What are good vegetarian options?
- Tell me about Korean cuisine
- What is a good high protein food?
- Tell me about Mediterranean food
- What are some comfort foods?
- What Thai dishes do you know?
- Tell me about desserts
- What are some Asian soups?
- Tell me about street food
- What are some Indonesian dishes?

All 15 queries successfully returned relevant sources and accurate AI responses.

## Version History

v1.0 - Local ChromaDB and Ollama Python CLI system
v2.0 - Cloud migration with Upstash Vector and Groq API
v3.0 - Full stack Next.js web application deployed on Vercel
