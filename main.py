from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# from config import settings
from schemas import TextRequest, QuizRequest

from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


app = FastAPI(
    title="EduGenie",
    description="Google Gemini Powered Learning Assistant",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "app": "EduGenie",
        "version": "1.0.0"
    }


@app.post("/qa")
async def qa(request: TextRequest):
    try:
        result = answer_question(request.text)

        return {
            "success": True,
            "task": "qa",
            "result": result
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )


@app.post("/explain")
async def explain(request: TextRequest):
    try:
        result = explain_concept(request.text)

        return {
            "success": True,
            "task": "explain",
            "result": result
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )


@app.post("/quiz")
async def quiz(request: QuizRequest):
    try:
        result = generate_quiz(
            request.text,
            request.count
        )

        return {
            "success": True,
            "task": "quiz",
            "result": result
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )


@app.post("/summarize")
async def summarize(request: TextRequest):
    try:
        result = summarize_text(request.text)

        return {
            "success": True,
            "task": "summarize",
            "result": result
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )


@app.post("/learn/recommendations")
async def recommendations(request: TextRequest):
    try:
        result = get_learning_recommendations(request.text)

        return {
            "success": True,
            "task": "recommend",
            "result": result
        }

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=str(exc)
        )