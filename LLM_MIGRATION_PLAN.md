# LLM Migration: Ollama → Groq

## Install Groq
```bash
pip3 install groq
```

## Create `groq_client.py`
```python
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class GroqLLMClient:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    
    def generate(self, prompt, max_tokens=1024):
        try:
            response = self.client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role": "user", "content": prompt}],
                max_completion_tokens=max_tokens,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
```

## Update `rag_run_upstash.py`

Add import at top:
```python
from groq_client import GroqLLMClient
```

Replace this section (around line 60):
```python
# Step 4: Generate answer with Ollama
try:
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": LLM_MODEL,
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"].strip()
except Exception as e:
    return f"❌ Error generating answer: {e}"
```

With this:
```python
# Step 4: Generate answer with Groq
try:
    llm = GroqLLMClient()
    return llm.generate(prompt)
except Exception as e:
    return f"❌ Error generating answer: {e}"
```

## Run It
```bash
# No need for Ollama anymore!
python3 rag_run_upstash.py
```

Done! Now using Groq (5x faster, cheaper, cloud-based).