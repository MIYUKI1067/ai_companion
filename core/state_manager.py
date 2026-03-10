import datetime

from simulation.activity_engine import get_current_activity


class StateManager:

    def __init__(self):

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

        now = datetime.datetime.now()

        return now.strftime("%Y-%m-%d %H:%M")


    def update_activity(self):

        event = get_current_activity()

        self.state["activity"] = event["event"]

        self.state["location"] = event["location"]


    def get_state(self):

        self.update_activity()

        self.state["current_time"] = self.get_time()

        return self.state


state_manager = StateManager()