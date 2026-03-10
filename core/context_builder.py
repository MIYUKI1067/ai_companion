import json
from memory.memory_manager import get_memories
from database.db_manager import get_recent_messages


def build_context(character, relationship, state):

    memories = get_memories()

    memory_text = "\n".join(memories)

    recent_chat = get_recent_messages(6)

    chat_text = ""

    for speaker, message in recent_chat:
        chat_text += f"{speaker}: {message}\n"

    context = f"""
角色資訊
姓名:{character['name']}
職業:{character['job']}
個性:{character['personality']}

關係狀態
階段:{relationship[1]}
好感度:{relationship[0]}

目前生活狀態
心情:{state['mood']}
活動:{state['activity']}

重要記憶
{memory_text}

最近聊天
{chat_text}
"""

    return context