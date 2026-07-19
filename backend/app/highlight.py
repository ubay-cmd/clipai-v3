from fastapi import APIRouter

router = APIRouter()

@router.get("/highlights")
def highlights():

    return {
        "clips": [
            {
                "start": 15,
                "end": 75,
                "score": 94,
                "title": "Rahasia yang Jarang Diketahui"
            },
            {
                "start": 120,
                "end": 180,
                "score": 91,
                "title": "Kesalahan yang Sering Dilakukan"
            }
        ]
    }