import random

EVENT_POOL = [

{
"name":"臨時加班",
"activity":"在醫院加班",
"mood":-0.2,
"energy":-0.2
},

{
"name":"和小芸吃晚餐",
"activity":"和小芸吃飯",
"mood":0.3,
"energy":-0.1
},

{
"name":"河濱跑步",
"activity":"河濱跑步",
"mood":0.4,
"energy":-0.2
},

{
"name":"外拍工作",
"activity":"外拍工作",
"mood":0.2,
"energy":-0.2
},

{
"name":"被病人家屬感謝",
"activity":"在醫院工作",
"mood":0.5,
"energy":-0.1
}

]


def generate_event():

    if random.random() < 0.2:

        return random.choice(EVENT_POOL)

    return None


def apply_event(state,event):

    state["activity"] = event["activity"]

    state["mood"] += event["mood"]

    state["energy"] += event["energy"]

    state["mood"] = max(-1,min(1,state["mood"]))

    state["energy"] = max(0,min(1,state["energy"]))

    return state