import json
from memory.memory_manager import get_memories


def build_prompt(player_input, character, relationship, state):

    memories = get_memories()

    memory_text = "\n".join(memories)

    system_prompt = f"""
你現在扮演角色：

姓名：{character['name']}
職業：{character['job']}
個性：{character['personality']}

你與玩家的關係：
階段：{relationship[1]}
好感度：{relationship[0]}

目前狀態：
心情：{state['mood']}
活動：{state['activity']}

角色長期記憶：
{memory_text}

請用LINE聊天方式自然回覆玩家。
語氣要符合角色個性。
"""

    return system_prompt