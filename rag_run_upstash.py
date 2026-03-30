import os
import json
from upstash_client import UpstashVectorClient
from groq_client import GroqLLMClient

# Constants
JSON_FILE = "foods.json"

# Initialize Upstash client
upstash = UpstashVectorClient()

# Load data
with open(JSON_FILE, "r", encoding="utf-8") as f:
    food_data = json.load(f)

# Prepare items for Upstash (add to metadata to store extra info)
items_to_upsert = []
for item in food_data:
    prepared_item = {
        "id": item["id"],
        "text": item["text"],
    }
    if "region" in item:
        prepared_item["region"] = item["region"]
        prepared_item["text"] += f" (Region: {item['region']})"
    if "type" in item:
        prepared_item["type"] = item["type"]
        prepared_item["text"] += f" (Type: {item['type']})"
    
    items_to_upsert.append(prepared_item)

# Upsert all items
if items_to_upsert:
    print(f"🆕 Adding {len(items_to_upsert)} documents to Upstash...")
    result = upstash.upsert(items_to_upsert)
    if result["success"]:
        print(f"✅ Successfully added {result['count']} items to Upstash Vector DB")
    else:
        print(f"❌ Error upserting: {result['error']}")

# RAG query function
def rag_query(question):
    # Step 1: Query Upstash (automatic embedding!)
    print("\n🧠 Retrieving relevant information to reason through your question...\n")
    
    results = upstash.query(question, top_k=5)
    
    if not results:
        return "❌ No relevant information found in the database."
    
    # Step 2: Show retrieved documents
    top_docs = [r["text"] for r in results]
    top_ids = [r["id"] for r in results]
    
    for i, doc in enumerate(top_docs):
        print(f"🔹 Source {i + 1} (ID: {top_ids[i]}):")
        print(f"    \"{doc}\"\n")

    print("📚 These seem to be the most relevant pieces of information to answer your question.\n")

    # Step 3: Build prompt from context
    context = "\n".join(top_docs)

    prompt = f"""Use the following context to answer the question.

Context:
{context}

Question: {question}
Answer:"""

    # Step 4: Generate answer with Groq
    try:
        llm = GroqLLMClient()
        return llm.generate(prompt)
    except Exception as e:
        return f"❌ Error generating answer: {e}"


# Interactive loop
print("\n🧠 RAG is ready. Ask a question (type 'exit' to quit):\n")
while True:
    question = input("You: ")
    if question.lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break
    answer = rag_query(question)
    print("🤖:", answer)
