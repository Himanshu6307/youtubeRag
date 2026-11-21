from pydantic import BaseModel
from fastapi import HTTPException
from src.rag.services.indexing.index import chunking
from src.rag.services.indexing.index import chromaEmbeded



class body(BaseModel):
    text:str
    videoId:str



def chunkAndEmbeded(req: Body):

    text = req.text
    videoId = req.videoId

    if not text.strip() or not videoId.strip():
        raise HTTPException(
            status_code=400,
            detail="Text and videoId are required"
        )

    try:
        chunk = chunking(text, videoId)

        if chunk is None:
            return {
                
                    "message": "Video chunked and embedded successfully",
                    "success": True
                }

        chromaEmbeded(chunk, videoId)

        return {
            "message": "Video chunked and embedded successfully",
            "success": True
        }

    except HTTPException:
        raise

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Indexing failed: {str(e)}"
        )



