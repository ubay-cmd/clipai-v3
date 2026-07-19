from .status import router as status_router
from .highlight import router as highlight_router
from fastapi import FastAPI
from .upload import router as upload_router

app = FastAPI(
    title="ClipAI V3"
)
app.include_router(status_router)
app.include_router(upload_router)

@app.get("/")
def root():
    return {
        "status": "online"
    }
app.include_router(highlight_router)