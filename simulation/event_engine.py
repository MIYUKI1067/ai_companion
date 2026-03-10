import random

EVENT_POOL = [

("今天臨時被要求加班", -0.3, 0.3),

("和小芸一起吃晚餐", 0.3, -0.1),

("今天跑步跑得很舒服", 0.4, -0.2),

("被病人家屬感謝", 0.5, -0.1),

("拍攝取消了", -0.2, 0.1)

]


def random_event():

    if random.random() < 0.2:

        return random.choice(EVENT_POOL)

    return None