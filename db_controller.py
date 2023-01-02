from .db import get_db

def insert_user(mail, username, password) -> bool:
    db = get_db()
    cursor = db.cursor()

    statement: str
    statement = "SELECT password FROM User WHERE username = (?);"
    cursor.execute(statement, [username])
    exist = cursor.fetchone()
    
    if exist is None:
        statement: str
        statement = "INSERT INTO User(mail, username, password) VALUES(?, ?, ?);"
        cursor.execute(statement, [mail, username, password])
        db.commit()
        db.close()
    return True

def insert_preference(cr_usnm, uid, op1, op2, op3, op4, op5) -> None:
    db = get_db()
    cursor = db.cursor()
    statement: str
    statement = "SELECT id FROM User WHERE username = (?);"
    cursor.execute(statement, [cr_usnm])
    exist = cursor.fetchone()
    
    if exist is not None:
        statement: str
        statement = "INSERT INTO Dashboard(school,base,positions,year,department,user_id) VALUES(?,?,?,?,?,?);"
        cursor.execute(statement, [op1,op2,op3,op4,op5,uid])

    db.commit()
    db.close()

def get_preferences(uid) -> None:
    db = get_db()
    cursor = db.cursor()
    stm: str
    stm = "SELECT * FROM Dashboard WHERE user_id = (?);"
    cursor.execute(stm, [uid])
    res = cursor.fetchall()
    
    db.commit()
    db.close()

    return res
