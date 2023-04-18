# Database for single-player highscores

import sqlite3

db = sqlite3.connect("scores.db") 
db.isolation_level = None 

def create_table():
    db.execute("CREATE TABLE IF NOT EXISTS Scores (id INTEGER PRIMARY KEY, player TEXT, score INTEGER)")

def insert_score(player, score):
    db.execute("INSERT INTO Scores (player, score) VALUES (?, ?)", (player, score))

def get_top3():
    a = db.execute("SELECT player, score FROM Scores ORDER BY score LIMIT 3").fetchall()
    return a

create_table()

insert_score("cosmo", 300)

a = get_top3

print(a)