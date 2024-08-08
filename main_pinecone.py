from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

pc = Pinecone(
    api_key = os.getenv("PINECONE_API_KEY")
)

index_name = "docs-quickstart-index"

# print(pc.list_indexes().names())
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name = index_name,
        dimension = 2,
        metric = "cosine",
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'
        )
    )