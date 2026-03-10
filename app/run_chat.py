import json

from core.chat_engine import chat

from simulation.schedule_engine import get_current_activity

from simulation.state_engine import update_mood, update_energy

from simulation.event_engine import generate_event, apply_event


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


    event = generate_event()

    if event:

        state = apply_event(state, event)

        print(f"\n[生活事件] {event['name']}\n")


    msg = input("你：")

    reply = chat(msg, character, state)

    print("許然：", reply)