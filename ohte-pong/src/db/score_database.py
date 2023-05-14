import sqlite3

db = sqlite3.connect("scores.db")
db.isolation_level = None 

test_db = sqlite3.connect("test.db") 
test_db.isolation_level = None

def create_tables():
    db.execute("""CREATE TABLE IF NOT EXISTS 
               Scores (id INTEGER PRIMARY KEY, 
               player TEXT, score INTEGER)""")
    
    test_db.execute("""CREATE TABLE IF NOT EXISTS 
               Scores (id INTEGER PRIMARY KEY, 
               player TEXT, score INTEGER)""")

def insert_score(player, score, db_name):
    conn = globals()[db_name]
    conn.execute("INSERT INTO Scores (player, score) VALUES (?, ?)", (player, score))

def get_top3(db_name):
    conn = globals()[db_name]
    a = conn.execute("SELECT player, score FROM Scores ORDER BY score DESC LIMIT 3").fetchall()
    return a

def clear(db_name):
    conn = globals()[db_name]
    conn.execute("DELETE FROM Scores")
