from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ollama import AsyncClient
import asyncio

app = FastAPI(title="Ollama API Wrapper")


class ChatRequest(BaseModel):
    prompt: str
    model: str = "deepseek-r1:8b"


class ChatResponse(BaseModel):
    response: str


@app.post("/chat", response_model=ChatResponse)
async def chat_with_ollama(chat: ChatRequest):
    try:
        client = AsyncClient()
        response = await client.generate(model=chat.model, prompt=chat.prompt)
        return {"response": response["response"]}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error communicating with Ollama: {str(e)}"
        )


# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
