import datetime
from simulation.life_timeline import life_timeline


def get_current_activity():

    now = datetime.datetime.now()

    current_time = now.strftime("%H:%M")

    timeline = life_timeline.get_timeline()

    current_event = timeline[0]

    for item in timeline:

        if item["time"] <= current_time:

            current_event = item

    return current_event