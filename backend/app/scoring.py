HOOK_WORDS = [
    "rahasia",
    "cara",
    "jangan",
    "ternyata",
    "kesalahan"
]

def score_text(text):

    score = 50

    for word in HOOK_WORDS:
        if word in text.lower():
            score += 10

    return min(score, 100)