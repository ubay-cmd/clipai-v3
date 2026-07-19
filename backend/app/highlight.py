from fastapi import APIRouter

router = APIRouter()

@router.get("/highlights")
def highlights():
    return {
        "clips": [
            {
                "start": 10,
                "end": 45,
                "score": 90
            }
        ]
    }