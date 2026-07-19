from fastapi import APIRouter
from .pipeline import run_pipeline

router = APIRouter()

@router.post("/pipeline/{project_id}")
def start_pipeline(project_id: str):
    return run_pipeline(project_id)