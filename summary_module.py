def summarize_text(text):
    if not text:
        return ""

    sentences = text.split(".")
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]

    if len(sentences) <= 3:
        return ". ".join(sentences) + "."

    return ". ".join(sentences[:3]) + "."