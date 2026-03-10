from openai import OpenAI
from core.prompt_builder import build_prompt
from database.db_manager import get_relationship

client = OpenAI()


def chat(player_input, character, state):

    relationship = get_relationship()

    prompt = build_prompt(
        player_input,
        character,
        relationship,
        state
    )

    response = client.chat.completions.create(

        model="gpt-4.1-mini",

        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": player_input}
        ]

    )

    return response.choices[0].message.content