from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import json

from core.chat_engine import chat
from simulation.schedule_engine import get_current_activity
from simulation.state_engine import update_mood, update_energy

app = FastAPI()

templates = Jinja2Templates(directory="ui/templates")

character = json.load(open("characters/xuran/profile.json"))

state = {
    "mood":0.2,
    "energy":0.8,
    "activity":get_current_activity()
}

class Message(BaseModel):
    text:str


@app.get("/",response_class=HTMLResponse)
def chat_page(request:Request):

    return templates.TemplateResponse(
        "chat.html",
        {"request":request}
    )


@app.post("/chat")
def chat_api(message:Message):

    state["activity"] = get_current_activity()

    state["mood"] = update_mood(state["mood"],state["activity"])

    state["energy"] = update_energy(state["energy"],state["activity"])

    reply = chat(message.text,character,state)

    return {"reply":reply}