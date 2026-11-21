from src.rag.config.textsplit import getSplit
from src.rag.config.chroma import getChroma
from langchain_core.documents import Document
from datetime import datetime, timedelta, timezone


def chunking(text: str, videoId: str) -> list[str]:

    vector_store = getChroma()

    result = vector_store.get(
        where={"source": videoId}
    )

    if result["ids"]:
        print(len(result["ids"]))
        return
    else:
        splitter = getSplit()
        texts: list[str] = splitter.split_text(text)


        expiresAt = (
                datetime.now(timezone.utc) + timedelta(days=7)
            ).timestamp()

        docs = []

        for text in texts:
            doc = Document(
                page_content=text,
                metadata={"source": videoId,"expiresAt": expiresAt}
            )
            docs.append(doc)

        print("chunking done")
        print(docs)
        return docs

def chromaEmbeded(chunks:[Document],videoId:str):

    vector_store = getChroma()

    result = vector_store.get(
        where={"source": videoId}
    )



    if result["ids"]:
        print(len(result["ids"])) 
        return
    else:
        vector_store.add_documents(
        documents=chunks,
        )

        print("Embedded Generating")
        return 

        
