import sqlite3
from score_database import create_table

db = sqlite3.connect("scores.db")
db.isolation_level = None

if __name__ == "__main__":
    create_table()
