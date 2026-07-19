from fastapi import APIRouter

router = APIRouter()

HOOK_WORDS = [
    "rahasia",
    "cara",
    "penting",
    "kesalahan",
    "ternyata",
    "jangan"
]

@router.get("/highlights")
def highlights():

    clips = [
        {
            "start": 10,
            "end": 45,
            "score": 90,
            "reason": "strong hook"
        }
    ]

    return {
        "clips": clips
    }