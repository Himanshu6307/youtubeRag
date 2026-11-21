from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = None

def getSplit():
    global text_splitter

    if text_splitter is None:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=150,
            chunk_overlap=20
        )

    return text_splitter