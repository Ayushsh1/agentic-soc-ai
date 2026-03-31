from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# use local embeddings (NO API KEY needed)
embeddings = HuggingFaceEmbeddings()

# initial memory
texts = [
    "Previous brute force attack from 192.168.1.10 blocked",
    "Port scanning activity detected from suspicious IP"
]

# create vector DB
db = FAISS.from_texts(texts, embeddings)

def search_memory(query):
    results = db.similarity_search(query, k=1)
    return results[0].page_content if results else "No similar incidents found"