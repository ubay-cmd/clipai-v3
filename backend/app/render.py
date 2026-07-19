from fastapi import APIRouter

router = APIRouter()

@router.post("/render")
def render_clip():

    return {
        "status": "rendered",
        "output": "outputs/clip.mp4"
    }