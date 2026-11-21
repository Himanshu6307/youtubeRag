from fastapi import APIRouter
from src.rag.controllers.chunkAndembeded import chunkAndEmbeded , body


router = APIRouter()

@router.post("/store")
def store(chunkBody:body):
    return chunkAndEmbeded(chunkBody)



