import sqlite3

DB_NAME = "companion.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS characters (
        id TEXT PRIMARY KEY,
        name TEXT,
        age INTEGER,
        job TEXT,
        personality TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS player_profile (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        nickname TEXT,
        hobbies TEXT,
        job TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS relationship (
        character_id TEXT,
        affection_score INTEGER,
        relationship_stage TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS life_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id TEXT,
        time TEXT,
        location TEXT,
        activity TEXT,
        mood REAL,
        energy REAL,
        stress REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS conversation (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id TEXT,
        speaker TEXT,
        message TEXT,
        time TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id TEXT,
        type TEXT,
        content TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character_id TEXT,
        time TEXT,
        type TEXT,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()