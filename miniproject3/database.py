#!/usr/bin/python

# standard library
import sqlite3 as sql

# connect to sqliteDB
conn = sql.connect('myrecipes.db')

def create_table():
    conn.execute('''CREATE TABLE IF NOT EXISTS myrecipes
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                thumbnail_url TEXT,
                label TEXT,
                ingredients TEXT,
                source_url TEXT)''')
    conn.commit()

# insert a recipe into the database
def insert_recipe(recipe):
    conn.execute('''INSERT INTO myrecipes (thumbnail_url, label, ingredients, source_url)
                    VALUES (?, ?, ?, ?)''', (recipe['thumbnail_url'], recipe['label'], '\n'.join(recipe['ingredients']), recipe['source_url']))
    conn.commit()

def close_connection():
    conn.close()

# call to create the table
create_table()
