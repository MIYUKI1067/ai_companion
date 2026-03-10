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


class AdminState(BaseModel):
    mood: float
    energy: float
    stress: float
    location: str
    activity: str


class AdminTime(BaseModel):
    time: str


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


@app.get("/admin", response_class=HTMLResponse)
def admin_page(request: Request):

    return templates.TemplateResponse(
        "admin.html",
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


@app.post("/admin/set_state")
def set_state(data: AdminState):

    state_manager.set_state_value("mood", data.mood)
    state_manager.set_state_value("energy", data.energy)
    state_manager.set_state_value("stress", data.stress)
    state_manager.set_state_value("location", data.location)
    state_manager.set_state_value("activity", data.activity)

    return {"status": "ok"}


@app.post("/admin/set_time")
def set_time(data: AdminTime):

    state_manager.set_time(data.time)

    return {"status": "ok"}