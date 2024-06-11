import sqlite3

conn = sqlite3.connect("lib/db/database.db")
cursor = conn.cursor()