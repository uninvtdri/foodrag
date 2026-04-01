import type { Metadata } from "next"

export const metadata: Metadata = {
  title: "Food RAG",
  description: "AI-powered food knowledge assistant",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
