from langchain_chroma import Chroma
from src.rag.model.model import getModel

def getChroma() -> Chroma:

    embeddings = getModel("tough")

    vector_store = Chroma(
        collection_name="youtube_rag",
        embedding_function=embeddings,
        persist_directory="./chroma_db"
    )

    return vector_store