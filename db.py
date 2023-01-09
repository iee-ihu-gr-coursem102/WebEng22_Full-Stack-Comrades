import sqlite3
import os
from pathlib import Path

#DATABASE_NAME = "C:\\Users\\Stella\\Documents\\GitHub\\WebEng22_Full-Stack-Comrades\\db.sqlite"
#DATABASE_NAME = '/home/nikolai/Downloads/Github/WebEng22_Full-Stack-Comrades/db.sqlite'
#DATABASE_NAME = 'db.sqlite'
dir_path = Path().absolute()
DATABASE_NAME = f'{dir_path}/db.sqlite'


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

