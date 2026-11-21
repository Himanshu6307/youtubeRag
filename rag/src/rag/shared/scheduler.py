from apscheduler.schedulers.background import BackgroundScheduler
from src.rag.services.indexing.cleanup import deleteExpiredChunks

scheduler = BackgroundScheduler()

def startScheduler():
    scheduler.add_job(
        deleteExpiredChunks,
        trigger="interval",
        hours=24,
        id="delete_expired_chunks",
        replace_existing=True
    )

    scheduler.start()