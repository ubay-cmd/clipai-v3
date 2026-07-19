from fastapi import FastAPI
from .upload import router as upload_router

app = FastAPI(
    title="ClipAI V3"
)

app.include_router(upload_router)

@app.get("/")
def root():
    return {
        "status": "online"
    }