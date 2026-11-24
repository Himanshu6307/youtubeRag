from fastapi import APIRouter
from src.rag.controllers.chunkAndembeded import chunkAndEmbeded , body
from src.rag.controllers.retriveTextAnswer import retriveAnswer , retriveBody


router = APIRouter()

@router.post("/store")
def store(chunkBody:body):
    return chunkAndEmbeded(chunkBody)

@router.post("/retrive")
def store(chunkBody:retriveBody):
    return retriveAnswer(chunkBody)



