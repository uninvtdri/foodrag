"use server"

import { ragQuery } from "../lib/rag"

export async function askFood(question: string) {
  try {
    const result = await ragQuery(question)
    return { success: true, ...result }
  } catch (error: any) {
    return { success: false, error: error.message }
  }
}
