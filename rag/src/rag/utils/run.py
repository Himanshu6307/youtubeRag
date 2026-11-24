from src.rag.config.chroma import getChroma

def testChroma():

    db = getChroma()

    data = db.get()

    print("Total documents:", len(data["ids"]))
    print("IDs:", data["ids"])
    print("Metadata:", data["metadatas"])
    print("Documents:", data["documents"])


testChroma()