import sqlite3

conn = sqlite3.connect("shop.db")  # Passe den Namen ggf. an!
cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [row[0] for row in cursor.fetchall()]
print("Tabellen in der Datenbank:", tables)