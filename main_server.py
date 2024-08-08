from fastapi import FastAPI
from langserve import add_routes
from main_openai_az import chain

app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)

add_routes(app, chain, path="/chain")

# Note@2024-08-08:
"""
LANGSERVE: ⚠️ Using pydantic 2.8.2. OpenAPI docs for invoke, batch, stream, stream_log endpoints will not be generated. 
API endpoints and playground should work as expected. 
If you need to see the docs, you can downgrade to pydantic 1. 
For example, `pip install pydantic==1.10.13`. See https://github.com/tiangolo/fastapi/issues/10360 for details.
"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8080)