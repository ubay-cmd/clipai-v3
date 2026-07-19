from .database import projects

def run_pipeline(project_id: str):

    project = projects.get(project_id)

    if not project:
        return {
            "error": "project not found"
        }

    return {
        "project_id": project_id,
        "steps": [
            "uploaded",
            "transcribed",
            "highlighted",
            "subtitled",
            "rendered"
        ],
        "status": "completed"
    }