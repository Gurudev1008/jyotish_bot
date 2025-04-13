import sqlite3

conn = sqlite3.connect("jyotish.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    tg_id INTEGER PRIMARY KEY,
    is_paid INTEGER DEFAULT 0
)
''')

conn.commit()
conn.close()
print("База данных создана.")
