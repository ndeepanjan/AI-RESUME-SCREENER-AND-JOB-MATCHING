import os
import psutil

process = psutil.Process(os.getpid())

def ram_mb():
    return process.memory_info().rss / (1024 * 1024)

print(f"Initial RAM: {ram_mb():.1f} MB")

print("\nLoading SentenceTransformer...")
from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer(
    "all-MiniLM-L6-v2",
    model_kwargs={"torch_dtype": "float16"}
)

embedder.eval()

print(f"After model + eval(): {ram_mb():.1f} MB")

print("\nRunning a real embedding...")
embedding = embedder.encode(
    ["This is a test resume for an AI engineer."]
)

print(f"After embedding generation: {ram_mb():.1f} MB")
print(f"Embedding shape: {embedding.shape}")

input("\nPress Enter to exit...")