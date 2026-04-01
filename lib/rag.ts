import { Index } from "@upstash/vector"
import Groq from "groq-sdk"

export async function ragQuery(question: string) {
  const index = new Index({
    url: process.env.UPSTASH_VECTOR_REST_URL!,
    token: process.env.UPSTASH_VECTOR_REST_TOKEN!,
  })

  const groq = new Groq({ apiKey: process.env.GROQ_API_KEY! })

  const results = await index.query({
    data: question,
    topK: 5,
    includeMetadata: true,
  })

  const sources = results.map((r: any) => r.metadata?.text || "")
  const context = sources.join("\n")

  const completion = await groq.chat.completions.create({
    model: "llama-3.1-8b-instant",
    messages: [
      { role: "system", content: "You are a food expert. Answer questions using the provided context." },
      { role: "user", content: `Context:\n${context}\n\nQuestion: ${question}` },
    ],
    temperature: 0.7,
  })

  return {
    answer: completion.choices[0].message.content,
    sources,
  }
}
