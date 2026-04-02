import json
from upstash_client import UpstashVectorClient

print('📊 Loading all food data...')
with open('foods.json') as f:
    items = json.load(f)

print(f'✅ Loaded {len(items)} items')

# Prepare enriched items
prepared = []
for item in items:
    new_text = item["text"]
    if "region" in item:
        new_text += f" (Region: {item['region']})"
    if "type" in item:
        new_text += f" (Type: {item['type']})"
    
    prepared.append({
        "id": item["id"],
        "text": new_text,
        "region": item.get("region", ""),
        "type": item.get("type", "")
    })

print(f'🚀 Uploading to Upstash Vector DB...')
upstash = UpstashVectorClient()
result = upstash.upsert(prepared)

if result["success"]:
    print(f'✅ SUCCESS! Uploaded {result["count"]} items to Upstash')
    print('\n🎯 Testing with sample queries:')
    
    queries = ["What is sinigang?", "Tell me about healthy foods", "What Filipino foods do you know?"]
    for q in queries:
        results = upstash.query(q, top_k=2)
        print(f'\n  Q: {q}')
        print(f'  ✓ Found {len(results)} relevant items')
        if results:
            print(f'    Top: {results[0]["text"][:70]}...')
else:
    print(f'❌ Error: {result["error"]}')
