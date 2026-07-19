from fastapi import FastAPI

app = FastAPI(
    title="ClipAI V3"
)

@app.get("/")
def root():
    return {
        "status": "online",
        "project": "ClipAI V3"
    }