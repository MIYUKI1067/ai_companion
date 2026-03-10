from openai import OpenAI
from database.db_manager import get_recent_messages
from memory.memory_manager import add_memory

client = OpenAI()


def summarize_day():

    messages = get_recent_messages(20)

    text = ""

    for speaker, msg in messages:
        text += f"{speaker}:{msg}\n"

    prompt = f"""
以下是今天的聊天紀錄

{text}

請整理成3條重要記憶
每條不超過20字
"""

    result = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role":"user","content":prompt}]
    )

    memories = result.choices[0].message.content.split("\n")

    for m in memories:
        if m.strip():
            add_memory("conversation_summary",m,2)