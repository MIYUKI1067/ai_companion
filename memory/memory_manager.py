import sqlite3

DB_NAME = "player.db"

def add_memory(type_,content,importance=1):

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO memory (type,content,importance) VALUES (?,?,?)",
        (type_,content,importance)
    )

    conn.commit()
    conn.close()


def get_memories(limit=5):

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        SELECT content
        FROM memory
        ORDER BY importance DESC,timestamp DESC
        LIMIT ?
    """,(limit,))

    rows = cur.fetchall()

    conn.close()

    return [r[0] for r in rows]