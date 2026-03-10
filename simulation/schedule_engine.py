import datetime


def get_current_activity():

    now = datetime.datetime.now()

    hour = now.hour


    if 0 <= hour < 7:
        return "睡覺"

    if 7 <= hour < 8:
        return "剛起床"

    if 8 <= hour < 9:
        return "通勤去醫院"

    if 9 <= hour < 12:
        return "在醫院工作"

    if 12 <= hour < 13:
        return "吃午餐"

    if 13 <= hour < 17:
        return "在醫院工作"

    if 17 <= hour < 18:
        return "下班通勤"

    if 18 <= hour < 20:
        return "晚餐時間"

    if 20 <= hour < 22:
        return "休息或運動"

    if 22 <= hour < 23:
        return "洗澡放鬆"

    return "準備睡覺"