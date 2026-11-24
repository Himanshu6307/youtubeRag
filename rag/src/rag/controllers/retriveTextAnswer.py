from pydantic import BaseModel
from fastapi import HTTPException
from src.rag.utils.retriveChunks import getRetrivedChunks


class retriveBody(BaseModel):
    que:str
    videoId:str


def retriveAnswer(req:retriveBody):

    question = req.que
    videoId = req.videoId

    if not question.strip() or not videoId.strip():
         raise HTTPException(
             status_code=400,
             detail="Text and videoId are required"
         )   

    final_txt = getRetrivedChunks(question , videoId)

    
    
