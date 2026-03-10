import datetime
from simulation.life_timeline import life_timeline


def get_current_activity(current_time_str):

    current_time = datetime.datetime.strptime(current_time_str, "%H:%M")

    timeline = life_timeline.get_timeline()

    events = []

    for item in timeline:

        event_time = datetime.datetime.strptime(item["time"], "%H:%M")

        events.append((event_time, item))

    events.sort(key=lambda x: x[0])

    current_event = events[-1][1]

    for i in range(len(events)):

        event_time, event = events[i]

        if current_time < event_time:

            if i == 0:
                current_event = events[-1][1]
            else:
                current_event = events[i-1][1]

            break

    return current_event