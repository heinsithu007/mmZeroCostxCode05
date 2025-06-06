#!/usr/bin/env python3
"""
Mock vLLM server for testing purposes
"""
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import json

app = FastAPI(title="Mock vLLM Server", version="1.0.0")

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    max_tokens: Optional[int] = 100
    temperature: Optional[float] = 0.7

class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: List[dict]

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/v1/models")
async def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "microsoft/DialoGPT-medium",
                "object": "model",
                "created": 1677610602,
                "owned_by": "microsoft"
            }
        ]
    }

@app.post("/v1/chat/completions")
async def chat_completions(request: ChatCompletionRequest):
    # Simple mock response
    user_message = request.messages[-1].content if request.messages else "Hello"
    
    mock_response = f"This is a mock response to: {user_message}"
    
    return {
        "id": "chatcmpl-mock123",
        "object": "chat.completion",
        "created": 1677652288,
        "model": request.model,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": mock_response
                },
                "finish_reason": "stop"
            }
        ],
        "usage": {
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)