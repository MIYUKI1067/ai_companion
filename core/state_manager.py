import datetime

from simulation.activity_engine import get_current_activity
from simulation.state_simulator import simulate_state


class StateManager:

    def __init__(self):

        self.override_time = None

        self.state = {

            "character": "許然",

            "affection_score": 70,
            "relationship_stage": "曖昧",

            "mood": 0.2,
            "energy": 0.8,
            "stress": 0.1,

            "location": "家裡",
            "activity": "休息",

            "last_event": "無",

            "current_time": self.get_time()

        }


    def get_time(self):

        if self.override_time:
            return self.override_time

        now = datetime.datetime.now()

        return now.strftime("%Y-%m-%d %H:%M")


    def get_time_hm(self):

        time_str = self.get_time()

        return time_str.split(" ")[1]


    def set_time(self, new_time):

        self.override_time = new_time


    def update_activity(self):

        current_time = self.get_time_hm()

        event = get_current_activity(current_time)

        self.state["activity"] = event["event"]

        self.state["location"] = event["location"]


    def update_state(self):

        self.state = simulate_state(self.state)


    def set_state_value(self, key, value):

        if key in self.state:
            self.state[key] = value


    def get_state(self):

        self.update_activity()

        self.update_state()

        self.state["current_time"] = self.get_time()

        return self.state


state_manager = StateManager()