from fastapi import APIRouter, UploadFile, File
from .project import create_project_id
from .database import projects
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_video(
    file: UploadFile = File(...)
):
    project_id = create_project_id()

    filepath = os.path.join(
        UPLOAD_DIR,
        f"{project_id}_{file.filename}"
    )

    with open(filepath, "wb") as f:
        content = await file.read()
        f.write(content)

    projects[project_id] = {
        "id": project_id,
        "filename": file.filename,
        "filepath": filepath,
        "status": "uploaded"
    }

    return projects[project_id]