import os
from upstash_vector import Index
from dotenv import load_dotenv

load_dotenv()

class UpstashVectorClient:
    def __init__(self):
        """Initialize Upstash Vector DB client"""
        self.url = os.getenv("UPSTASH_VECTOR_REST_URL")
        self.token = os.getenv("UPSTASH_VECTOR_REST_TOKEN")
        
        if not self.url or not self.token:
            raise ValueError("UPSTASH_VECTOR_REST_URL and UPSTASH_VECTOR_REST_TOKEN env vars required")
        
        self.index = Index(url=self.url, token=self.token)
    
    def upsert(self, items):
        """Add items to Upstash (auto-embeds text)"""
        try:
            vectors = []
            for item in items:
                vectors.append({
                    "id": str(item["id"]),
                    "data": item["text"],
                    "metadata": {
                        "text": item["text"],
                        "region": item.get("region", ""),
                        "type": item.get("type", "")
                    }
                })
            
            result = self.index.upsert(vectors=vectors)
            return {"success": True, "count": len(vectors), "result": result}
        except Exception as e:
            print(f"❌ Upsert error: {e}")
            return {"success": False, "error": str(e)}
    
    def query(self, question, top_k=3):
        """Search for similar items (auto-embeds question)"""
        try:
            results = self.index.query(
                data=question,
                top_k=top_k,
                include_metadata=True
            )
            
            formatted = []
            for result in results:
                formatted.append({
                    "id": result.id,
                    "text": result.metadata.get("text", result.metadata.get("data", "")),
                    "score": result.score,
                    "region": result.metadata.get("region", ""),
                    "type": result.metadata.get("type", "")
                })
            
            return formatted
        except Exception as e:
            print(f"❌ Query error: {e}")
            return []
