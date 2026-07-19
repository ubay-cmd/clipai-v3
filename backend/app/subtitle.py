def generate_srt(segments):

    srt = ""

    for i, seg in enumerate(segments, start=1):

        srt += f"{i}\n"
        srt += (
            f"00:00:{seg['start']:02},000 --> "
            f"00:00:{seg['end']:02},000\n"
        )

        srt += seg["text"] + "\n\n"

    return srt