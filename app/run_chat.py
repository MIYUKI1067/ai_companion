import json

from core.chat_engine import chat

from simulation.schedule_engine import get_current_activity

from simulation.state_engine import update_mood, update_energy


character = json.load(open("characters/xuran/profile.json"))


state = {

    "mood": 0.2,

    "energy": 0.8,

    "activity": get_current_activity()

}


while True:

    state["activity"] = get_current_activity()

    state["mood"] = update_mood(state["mood"], state["activity"])

    state["energy"] = update_energy(state["energy"], state["activity"])


    msg = input("你：")


    reply = chat(msg, character, state)


    print("許然：", reply)