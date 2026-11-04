class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.username = name
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.username}"