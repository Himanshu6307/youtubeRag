from datetime import datetime, timezone
from src.rag.config.chroma import getChroma

def deleteExpiredChunks():

    vector_store = getChroma()

    now = datetime.now(timezone.utc).timestamp()

    vector_store.delete(
        where={
            "expiresAt": {
                "$lt": now
            }
        }
    )

    print("Expired chunks deleted")