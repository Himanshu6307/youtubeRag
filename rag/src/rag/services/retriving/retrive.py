from src.rag.config.chroma import getChroma

def getRetriever(videoId: str):

    print(videoId)

    vector_store = getChroma()

    retriever = vector_store.as_retriever(
        search_kwargs={
            "k": 10,
            "filter": {
                "source": videoId
            }
        }
    )

    return retriever