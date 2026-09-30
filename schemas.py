from pydantic import BaseModel

class TextRequest(BaseModel):
    text: str

class QuizRequest(BaseModel):
    text: str
    num_questions: int = 5
