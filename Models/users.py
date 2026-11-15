from datetime import datetime
from typing import Optional

class User:
    def __init__(self, user_id:Optional[int], name, email, password, created_at:Optional[datetime], level:str='beginner'):
        self.user_id = user_id
        self.username = name
        self.email = email
        self.password = password
        self.created_at = created_at
        self.level = level