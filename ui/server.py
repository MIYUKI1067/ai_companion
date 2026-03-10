from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

import json

from core.chat_engine import chat
from core.state_manager import state_manager
from simulation.life_timeline import life_timeline


app = FastAPI()

templates = Jinja2Templates(directory="ui/templates")


with open("characters/xuran/profile.json", "r", encoding="utf-8") as f:
    character = json.load(f)


class Message(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
def chat_page(request: Request):

    return templates.TemplateResponse(
        "chat.html",
        {"request": request}
    )


@app.get("/dashboard", response_class=HTMLResponse)
def dashboard_page(request: Request):

    return templates.TemplateResponse(
        "dashboard.html",
        {"request": request}
    )


@app.post("/chat")
def chat_api(message: Message):

    state = state_manager.get_state()

    reply = chat(message.text, character, state)

    return {"reply": reply}


@app.get("/api/state")
def get_state():

    return state_manager.get_state()


@app.get("/api/life")
def get_life():

    return life_timeline.get_timeline()