from fastapi import APIRouter

router = APIRouter()

@router.get("/transcribe/{project_id}")
def transcribe(project_id: str):
    return {
        "project_id": project_id,
        "segments": [
            {
                "start": 0,
                "end": 5,
                "text": "Halo semuanya"
            },
            {
                "start": 5,
                "end": 10,
                "text": "Selamat datang di ClipAI"
            }
        ]
    }