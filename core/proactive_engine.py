import time
from database.db_manager import get_relationship


def should_proactive(last_chat_time):

    affection, stage = get_relationship()

    now = time.time()

    diff = now - last_chat_time

    if affection > 70 and diff > 43200:
        return True

    if affection > 40 and diff > 86400:
        return True

    return False