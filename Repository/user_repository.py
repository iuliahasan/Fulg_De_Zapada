from Database.database import get_connection
from Models.users import User

def create_user(username, password, level='beginner'):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        (cursor.execute('''INSERT INTO Utilizatori (username, password, 
            current_level, created_at) VALUES (:1, :2, :3, CURRENT_TIMESTAMP)'''),
            [username, password, level])
        connection.commit()
    finally:
        cursor.close()
        connection.close()

def find_by_username(username, password):
    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute('''SELECT userId, username, password, current_level, created_at
        FROM Utilizatori WHERE username = :1'''), [username]
        record = cursor.fetchone()

        if record:
            return User(
                user_id=record[0],
                name=record[1],
                email=record[2],
                password=record[3],
                created_at=record[4],
                level=record[5]
            )

        return None
    finally:
        cursor.close()
        connection.close()