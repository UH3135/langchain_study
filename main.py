from chain import chain
from langchain_teddynote import logging
from fastapi import FastAPI
from langserve import add_routes

app = FastAPI()
add_routes(app, chain, path="/chat")

logging.langsmith("llm_study")


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(app, host="localhost", port=8000)
    # http://localhost:8000/chat/playground/
    # 위 링크에 접속