import sqlite3

connection = sqlite3.connect('usersData.db')

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL,
        Username TEXT NOT NULL,      
        Password TEXT NOT NULL               
    );
               """)

print("Database Connected Successfully")
