import json
from core.chat_engine import chat
from simulation.life_simulator import get_activity
from memory.memory_manager import add_memory, get_memories

add_memory("player_fact","玩家喜歡棒球",5)

print(get_memories())


character = json.load(open("characters/xuran/profile.json"))

state = {
 "mood":0.2,
 "activity":get_activity()
}

while True:

    msg = input("你：")

    reply = chat(msg,character,state)

    print("許然：",reply)