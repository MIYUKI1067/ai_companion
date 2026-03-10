from core.character_manager import load_character
from database.database_manager import init_database

init_database()

character = load_character("xuran")

print(character)