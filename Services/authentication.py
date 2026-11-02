from Repository.user_repository import find_by_username

def authenticate(username, password):
    user = find_by_username(username)

    if user is None:
        return False

    return user['password'] == password

def register(username, password):
    pass