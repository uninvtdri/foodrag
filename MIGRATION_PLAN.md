# Migration Plan: ChromaDB → Upstash Vector DB

## Quick Overview
Replace local ChromaDB with cloud-hosted Upstash Vector DB. Upstash automatically embeds text, so you don't need Ollama for embeddings anymore.

---

## What Changes

| | ChromaDB | Upstash |
|---|---|---|
| Embedding | Manual (call Ollama) | Automatic (built-in) |
| Storage | Local folder | Cloud API |
| Setup | Complex | Simple |

---

## Steps to Migrate

### 1. Install Dependencies
```bash
pip3 install upstash-vector
```

### 2. Create `upstash_client.py`
Simple wrapper for Upstash operations:

```python
import os
from upstash_vector import Index

class UpstashVectorClient:
    def __init__(self):
        self.index = Index(
            url=os.getenv("UPSTASH_VECTOR_URL"),
            token=os.getenv("UPSTASH_VECTOR_TOKEN")
        )
    
    def upsert(self, items):
        """Add items to Upstash (auto-embeds text)"""
        vectors = []
        for item in items:
            vectors.append({
                "id": item["id"],
                "text": item["text"],
                "metadata": {
                    "region": item.get("region"),
                    "type": item.get("type")
                }
            })
        return self.index.upsert(vectors=vectors)
    
    def query(self, question, top_k=3):
        """Search for similar items (auto-embeds question)"""
        results = self.index.query(
            data=question,
            top_k=top_k,
            include_metadata=True
        )
        return results
```

### 3. Update `rag_run.py`
Replace ChromaDB code:

**OLD:**
```python
import chromadb

chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_or_create_collection(name="foods")

# Manual embedding call
emb = get_embedding(text)
collection.add(documents=[text], embeddings=[emb], ids=[id])

# Manual embedding in query
query_emb = get_embedding(question)
results = collection.query(query_embeddings=[query_emb], n_results=3)
```

**NEW:**
```python
from upstash_client import UpstashVectorClient

upstash = UpstashVectorClient()

# No embedding needed - just pass text
upstash.upsert([{"id": id, "text": text}])

# No embedding needed - just pass question
results = upstash.query(question, top_k=3)
```

### 4. Test Everything
```python
# Test upsert
from upstash_client import UpstashVectorClient
import json

upstash = UpstashVectorClient()

with open("foods.json") as f:
    items = json.load(f)

upstash.upsert(items[:5])  # Test with 5 items first
print("✅ Upsert works")

# Test query
results = upstash.query("What is sinigang?")
print(f"Found {len(results)} results")
```

### 5. Migrate All Data
```python
# In a script or terminal
with open("foods.json") as f:
    all_items = json.load(f)

upstash.upsert(all_items)
print(f"✅ Migrated {len(all_items)} items")
```

---

## Environment Setup

Add to `.env`:
```
UPSTASH_VECTOR_URL=your_url_here
UPSTASH_VECTOR_TOKEN=your_token_here
```

---

## Keep or Remove Files

**Keep (as backup):**
- `rag_run.py` - old ChromaDB version
- `chroma_db/` - old data folder

**Remove Eventually:**
- Ollama embedding calls
- `chromadb` import

---

## That's It!

Once done:
- Text search works automatically (Upstash embeds it)
- No local Ollama embedding service needed
- Everything in the cloud
- Same functionality, simpler code

