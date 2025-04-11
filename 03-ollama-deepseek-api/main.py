from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx

app = FastAPI()
OLLAMA_URL = "http://localhost:11434"


class ChatRequest(BaseModel):
    prompt: str
    model: str = "deepseek-r1:8b"


@app.post("/chat")
async def chat_with_ollama(chat: ChatRequest):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": chat.model,
                "prompt": chat.prompt,
                "stream": False,
            },
        )
        data = response.json()
        return {"response": data.get("response")}
