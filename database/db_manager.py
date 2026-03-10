import sqlite3

DB_NAME = "player.db"

def get_conn():
    return sqlite3.connect(DB_NAME)

def get_relationship():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT affection_score, stage FROM relationship LIMIT 1")
    row = cur.fetchone()
    conn.close()
    return row

def update_affection(score):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE relationship SET affection_score=?", (score,))
    conn.commit()
    conn.close()

def save_message(speaker, message):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO conversation (speaker,message) VALUES (?,?)",
        (speaker,message)
    )
    conn.commit()
    conn.close()