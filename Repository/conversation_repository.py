from Database.database import get_connection
from Models.conversation import Conversation

def save_conversation(username, question, answer):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute('''INSERT INTO Conversatii(username, question, answer, time) VALUES (:1, :2, :3, CURRENT_TIMESTAMP)''',
                   [username, question, answer])
        connection.commit()
    finally:
        cursor.close()
        connection.close()

def get_conversations_by_user(username):
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute('''SELECT * FROM Conversatii WHERE username = :1 ORDER BY time ASC''', [username])
        conversations = []

        for record in cursor.fetchall():
            conversation = Conversation(record[0], record[1], record[2],
                                        record[3], record[4])
            conversations.append(conversation)

        return conversations
    finally:
        cursor.close()
        connection.close()