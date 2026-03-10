import datetime

def get_activity():

    hour = datetime.datetime.now().hour

    if 0 <= hour < 7:
        return "睡覺"

    if 7 <= hour < 9:
        return "準備上班"

    if 9 <= hour < 17:
        return "在醫院工作"

    if 17 <= hour < 19:
        return "下班回家"

    if 19 <= hour < 22:
        return "休息或運動"

    return "準備睡覺"