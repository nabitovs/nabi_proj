import sqlite3

conn = sqlite3.connect('game_database.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM players")
rows = cursor.fetchall()
conn.close()

print(rows)
