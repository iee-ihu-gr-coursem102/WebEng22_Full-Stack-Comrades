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


def insert_preference(cr_usnm) -> None:
    db = get_db()
    cursor = db.cursor()
    statement: str
    statement = "SELECT username FROM User WHERE username = (?);"
    cursor.execute(statement, [cr_usnm])
    exist = cursor.fetchone()
    
    if exist is not None:
        insert_university(db, cursor, "ΑΠΘ", cr_usnm)


#def insert_city():
#
#

def insert_university(db, cursor, uni, cr_usnm) -> bool:
    statement: str
    statement = "INSERT INTO Preference(university, user_id) VALUES(?, ?);"
    cursor.execute(statement, [uni, cr_usnm])
    db.commit()
    db.close()
    return True



#def insert_department():
#
#

#def insert_year():
#
#

#def insert_base():


