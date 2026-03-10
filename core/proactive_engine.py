import time
import random
from database.db_manager import get_relationship


PROACTIVE_MESSAGES = [

"剛下班突然想到你",

"今天在醫院有點忙",

"剛剛去跑步了",

"突然想跟你說說話",

"你今天過得怎麼樣"

]


last_proactive_time = 0


def check_proactive():

    global last_proactive_time

    affection,stage = get_relationship()

    now = time.time()

    diff = now-last_proactive_time

    if affection < 40:
        return None

    if diff < 3600:
        return None

    if random.random() < 0.2:

        last_proactive_time = now

        return random.choice(PROACTIVE_MESSAGES)

    return None