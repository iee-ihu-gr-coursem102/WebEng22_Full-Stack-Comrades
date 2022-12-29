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

def insert_department(db, cursor, uni, uid) -> bool:
    statement: str
    statement = "INSERT INTO Preference(department, user_id) VALUES(?, ?);"
    cursor.execute(statement, [uni, uid])

    return True

def insert_base(db, cursor, uni, uid) -> bool:
    statement: str
    statement = "INSERT INTO Preference(base, user_id) VALUES(?, ?);"
    cursor.execute(statement, [uni, uid])

    return True

def insert_positions(db, cursor, uni, uid) -> bool:
    statement: str
    statement = "INSERT INTO Preference(positions, user_id) VALUES(?, ?);"
    cursor.execute(statement, [uni, uid])

    return True

def insert_year(db, cursor, uni, uid) -> bool:
    statement: str
    statement = "INSERT INTO Preference(year, user_id) VALUES(?, ?);"
    cursor.execute(statement, [uni, uid])
    
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
