import sqlite3
DATABASE_NAME = "C:\\Users\\Stella\\Documents\\GitHub\\WebEng22_Full-Stack-Comrades\\db.sqlite"
#/home/nikolai/Downloads/Github/WebEng22_Full-Stack-Comrades/db.sqlite


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

