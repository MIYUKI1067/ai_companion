from core.context_builder import build_context


def build_prompt(player_input, character, relationship, state):

    context = build_context(character, relationship, state)

    system_prompt = f"""
你正在扮演角色。

{context}

請用自然的LINE聊天語氣回覆玩家。
"""

    return system_prompt