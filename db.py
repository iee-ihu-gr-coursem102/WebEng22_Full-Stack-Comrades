import sqlite3
import os
from pathlib import Path

#DATABASE_NAME = 'db.sqlite'
dir_path = Path().absolute()
DATABASE_NAME = f'{dir_path}/db.sqlite'


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

