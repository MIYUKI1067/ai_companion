import random


ACTIVITY_EFFECT = {

    "睡覺": {
        "mood": 0.1,
        "energy": 0.3,
        "stress": -0.1
    },

    "上班": {
        "mood": -0.05,
        "energy": -0.1,
        "stress": 0.1
    },

    "午餐": {
        "mood": 0.1,
        "energy": 0.1,
        "stress": -0.05
    },

    "下班": {
        "mood": 0.1,
        "energy": 0.05,
        "stress": -0.1
    },

    "跑步": {
        "mood": 0.2,
        "energy": -0.1,
        "stress": -0.1
    },

    "回家": {
        "mood": 0.05,
        "energy": 0.05,
        "stress": -0.1
    }

}


def clamp(value, min_value, max_value):

    return max(min_value, min(value, max_value))


def simulate_state(state):

    activity = state["activity"]

    effect = ACTIVITY_EFFECT.get(activity)

    if effect is None:
        return state

    mood = state["mood"]
    energy = state["energy"]
    stress = state["stress"]

    mood += effect["mood"] + random.uniform(-0.02, 0.02)
    energy += effect["energy"] + random.uniform(-0.02, 0.02)
    stress += effect["stress"] + random.uniform(-0.02, 0.02)

    state["mood"] = clamp(mood, -1, 1)
    state["energy"] = clamp(energy, 0, 1)
    state["stress"] = clamp(stress, 0, 1)

    return state