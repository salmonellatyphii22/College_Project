from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.models import PromptRequest, PromptResponse
from app.classifier import classify
from app.responder import generate_response
from app.utils import save_history

app = FastAPI(title="Prompt Companion Tool")

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates folder
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )
    
@app.post("/process", response_model=PromptResponse)
async def process(prompt: PromptRequest):

    category = classify(prompt.prompt)

    response = generate_response(category)

    save_history(prompt.prompt, category)

    return PromptResponse(
        category=category,
        response=response
    )