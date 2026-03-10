import json
from memory.memory_manager import get_memories

memories = get_memories()

memory_text = "\n".join(memories)

def build_prompt(player_input, character, relationship, state):

    system = f"""
你是角色：{character['name']}
職業：{character['job']}
個性：{character['personality']}

目前關係階段：{relationship[1]}
好感度：{relationship[0]}

當前心情：{state['mood']}
目前活動：{state['activity']}

角色記憶：
{memory_text}

請用自然訊息方式回覆玩家。
"""

    user = player_input

    return system + "\n玩家：" + user