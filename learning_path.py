def get_learning_recommendations(text):
    if not text:
        return []

    return [
        {
            "topic": text,
            "recommendation": "Review the basic concepts first, then practice with examples and quizzes."
        }
    ]
    