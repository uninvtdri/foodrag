"use client"

import { useState } from "react"
import { askFood } from "./actions"

export default function Home() {
  const [question, setQuestion] = useState("")
  const [answer, setAnswer] = useState("")
  const [sources, setSources] = useState<string[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    if (!question.trim()) return
    setLoading(true)
    setError("")
    setAnswer("")
    setSources([])
    const result = await askFood(question)
    if (result.success) {
      setAnswer(result.answer || "")
      setSources(result.sources || [])
    } else {
      setError(result.error || "Something went wrong")
    }
    setLoading(false)
  }

  return (
    <main style={{ maxWidth: "800px", margin: "0 auto", padding: "20px", fontFamily: "sans-serif" }}>
      <h1 style={{ color: "#e67e22" }}>🍽️ Food RAG</h1>
      <p>AI-powered food knowledge assistant</p>
      <form onSubmit={handleSubmit}>
        <input
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask about food..."
          style={{ width: "80%", padding: "10px", fontSize: "16px" }}
        />
        <button type="submit" disabled={loading} style={{ padding: "10px 20px", marginLeft: "10px", background: "#e67e22", color: "white", border: "none", cursor: "pointer" }}>
          {loading ? "..." : "Send"}
        </button>
      </form>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {sources.length > 0 && (
        <div style={{ marginTop: "20px", padding: "15px", background: "#f9f9f9", borderRadius: "8px" }}>
          <h3>📚 Sources</h3>
          {sources.map((s, i) => <p key={i}>🔹 {s}</p>)}
        </div>
      )}
      {answer && (
        <div style={{ marginTop: "20px", padding: "15px", background: "#fff3e0", borderRadius: "8px" }}>
          <h3>🤖 AI Response</h3>
          <p>{answer}</p>
        </div>
      )}
    </main>
  )
}
