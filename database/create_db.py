import sqlite3

conn = sqlite3.connect("player.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS memory (
id INTEGER PRIMARY KEY AUTOINCREMENT,
type TEXT,
content TEXT,
importance INTEGER,
timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS relationship (
id INTEGER PRIMARY KEY,
affection_score INTEGER,
stage TEXT
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS conversation (
id INTEGER PRIMARY KEY,
speaker TEXT,
message TEXT,
timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS ai_state (
id INTEGER PRIMARY KEY,
mood REAL,
energy REAL,
stress REAL,
location TEXT,
activity TEXT
)
""")

cur.execute("""
INSERT OR IGNORE INTO relationship VALUES (1,50,'熟識')
""")

cur.execute("""
INSERT OR IGNORE INTO ai_state VALUES (1,0.2,0.8,0.1,'醫院','上班')
""")

conn.commit()
conn.close()

print("Database ready")