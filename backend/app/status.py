from fastapi import APIRouter
from .database import projects

router = APIRouter()

@router.get("/project/{project_id}")
def project_status(project_id: str):
    return projects.get(
        project_id,
        {"error": "not found"}
    )