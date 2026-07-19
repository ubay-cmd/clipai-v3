from fastapi import APIRouter

router = APIRouter()

@router.get("/transcribe/{project_id}")
def transcribe(project_id: str):
    return {
        "project_id": project_id,
        "status": "transcribed",
        "segments": [
            {
                "start": 0,
                "end": 5,
                "text": "Halo semuanya"
            }
        ]
    }