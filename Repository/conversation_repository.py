from Database.database import get_connection
from Models.conversation import Conversation

def save_conversation(question, answer):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO Conversatii(question, answer, time) VALUES (:1, :2, CURRENT_TIMESTAMP())''',
                   [question, answer])
    connection.commit()
    connection.close()

def get_conversations_by_user(username):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Conversatii WHERE username = :1 ''', [username])
    conversations = []

    for record in cursor.fetchall():
        conversation = Conversation(record[0], record[1], record[2],
                                    record[3], record[4])
        conversations.append(conversation)

    cursor.close()
    connection.close()

    return conversations