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

index = pc.Index(index_name)

index.upsert(
    vectors=[
        {"id": "vec1", "values": [1.0, 1.5]},
        {"id": "vec2", "values": [2.0, 1.0]},
        {"id": "vec3", "values": [0.1, 3.0]},
    ],
    namespace="ns1"
)

index.upsert(
    vectors=[
        {"id": "vec1", "values": [1.0, -2.5]},
        {"id": "vec2", "values": [3.0, -2.0]},
        {"id": "vec3", "values": [0.5, -1.5]},
    ],
    namespace="ns2"
)

print(index.describe_index_stats())

query_result1 = index.query(
    namespace="ns1",
    vector=[1.0, 1.5],
    top_k=3,
    include_values=True
)

print(query_result1)

query_result2 = index.query(
    namespace="ns2",
    vector=[1.0,-2.5],
    top_k=3,
    include_values=True
)

print(query_result2)

pc.delete_index(index_name)