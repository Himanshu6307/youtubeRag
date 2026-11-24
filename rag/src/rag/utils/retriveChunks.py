from src.rag.services.retriving.retrive import getRetriever


def getRetrivedChunks(question:str , videoId:str) -> str:


    retriver = getRetriever(videoId)

    chunks = retriver.invoke(question)

    # print("Chunks:", chunks)
    # print("Chunks length:", len(chunks))

    final_text = ""

    for doc in chunks:
        text = doc.page_content
        start = doc.metadata["start"]

        final_text += f"{start} : {text}\n"


    print("retrived chunks chala")
    print("final text",final_text)

    return final_text
    
