from langchain_groq import ChatGroq
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from src.rag.shared.settings import GROQ_API_KEY
from src.rag.shared.settings import LLM_MODEL
from src.rag.shared.settings import EMBEDDING_MODEL
from src.rag.shared.settings import GOOGLE_API_KEY


model = ChatGroq(
    model=LLM_MODEL,
    api_key=GROQ_API_KEY,
    temperature=0,
    max_tokens=None,
)


embeddings = GoogleGenerativeAIEmbeddings(
    model=EMBEDDING_MODEL,
    google_api_key=GOOGLE_API_KEY
)



def getModel(simple: str):
    if simple == "simple":
        return model
    else:
        return embeddings