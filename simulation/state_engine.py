import random

def update_mood(current_mood, stress):
    change = random.uniform(-0.1,0.1)

    if stress > 0.7:
        change -= 0.1

    new_mood = current_mood + change

    return max(-1,min(1,new_mood))


def update_energy(current_energy):
    drain = random.uniform(0.05,0.1)

    new_energy = current_energy - drain

    return max(0,new_energy)


def update_stress(current_stress):
    change = random.uniform(-0.05,0.1)

    new_stress = current_stress + change

    return max(0,min(1,new_stress))