from database.database_manager import get_connection


def create_character(character_id, name, age, job, personality):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO characters (id, name, age, job, personality)
        VALUES (?, ?, ?, ?, ?)
        """,
        (character_id, name, age, job, personality)
    )

    conn.commit()
    conn.close()

    print(f"Character {name} created.")


def load_character(character_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM characters WHERE id = ?
        """,
        (character_id,)
    )

    character = cursor.fetchone()

    conn.close()

    if character is None:
        print("Character not found")
        return None

    return dict(character)