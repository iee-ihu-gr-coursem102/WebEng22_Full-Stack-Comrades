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

def insert_preference(cr_usnm, uid, op1, op2, op3, op4) -> None:
    db = get_db()
    cursor = db.cursor()
    statement: str
    statement = "SELECT id FROM User WHERE username = (?);"
    cursor.execute(statement, [cr_usnm])
    exist = cursor.fetchone()
    
    if exist is not None:
        statement: str
        statement = "INSERT INTO Preference(positions,department,year,base,user_id) VALUES(?,?,?,?,?);"
        cursor.execute(statement, [op1,op2,op3,op4,uid])

    db.commit()
    db.close()

def get_preferences(uid) -> None:
    db = get_db()
    cursor = db.cursor()
    s1: str
    s2: str
    s3: str
    s4: str
    s1 = "SELECT DISTINCT positions FROM Preference WHERE user_id = (?);"
    cursor.execute(s1, [uid])
    ps = cursor.fetchall()
    s2 = "SELECT DISTINCT department FROM Preference WHERE user_id = (?);"
    cursor.execute(s2, [uid])
    de = cursor.fetchall()
    s3 = "SELECT DISTINCT year FROM Preference WHERE user_id = (?);"
    cursor.execute(s3, [uid])
    ye = cursor.fetchall()
    s4 = "SELECT DISTINCT base FROM Preference WHERE user_id = (?);"
    cursor.execute(s4, [uid])
    ba = cursor.fetchall()
    
    db.commit()
    db.close()

    return ps, de, ye, ba