import random


def update_mood(mood, activity):

    if activity == "運動":
        mood += 0.2

    if activity == "在醫院工作":
        mood -= random.uniform(0.05, 0.1)

    if activity == "睡覺":
        mood += 0.1

    return max(-1, min(1, mood))


def update_energy(energy, activity):

    if activity == "睡覺":
        energy += 0.3

    if activity == "在醫院工作":
        energy -= 0.1

    if activity == "運動":
        energy -= 0.15

    return max(0, min(1, energy))