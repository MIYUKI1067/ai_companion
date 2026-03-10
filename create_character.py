from core.character_manager import create_character
from database.database_manager import init_database

init_database()

create_character(
    "xuran",
    "許然",
    27,
    "護理師",
    "溫柔、理性、情緒穩定"
)