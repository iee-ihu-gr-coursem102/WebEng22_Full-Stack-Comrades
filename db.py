import sqlite3
DATABASE_NAME = "/home/nikolai/Downloads/GitLab/uniview/db.sqlite"

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

