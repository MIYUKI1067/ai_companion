import datetime


class LifeTimeline:

    def __init__(self):

        self.timeline = []

        self.generate_default_day()


    def generate_default_day(self):

        self.timeline = [

            {"time": "08:30", "event": "上班", "location": "台北醫院"},
            {"time": "12:00", "event": "午餐", "location": "醫院餐廳"},
            {"time": "17:30", "event": "下班", "location": "醫院"},
            {"time": "19:00", "event": "跑步", "location": "河濱公園"},
            {"time": "21:00", "event": "回家", "location": "租屋處"},
            {"time": "23:30", "event": "睡覺", "location": "家裡"}

        ]


    def get_timeline(self):

        return self.timeline


life_timeline = LifeTimeline()