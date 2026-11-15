from datetime import datetime
from typing import Optional

class Conversation:
    def __init__(self, conversation_id:Optional[int], username, question, answer, time:datetime):
        self.conversation_id = conversation_id
        self.username = username
        self.question = question
        self.answer = answer
        self.time = time