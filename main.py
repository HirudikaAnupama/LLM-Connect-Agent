from fastapi import FastAPI
from app.routers import llm, chat

app = FastAPI(title="LLM Connect Agent API", version="1.0.0")

app.include_router(llm.router, prefix="/api/llm", tags=["LLM"])
app.include_router(chat.router, prefix="/api/chat", tags=["Chat"])




