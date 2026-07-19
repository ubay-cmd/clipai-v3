from pydantic import BaseModel

class Project(BaseModel):
    id: str
    filename: str
    status: str