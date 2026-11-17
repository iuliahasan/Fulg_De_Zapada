from Repository.user_repository import find_by_username, create_user

import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def authenticate(username, password):
    user = find_by_username(username, password)

    if user is None:
        return False

    return user.password == hash_password(password)

def register(username, password):
    if not username or not password:
        return False

    existing_user = find_by_username(username, password)

    if existing_user is not None:
        return False

    hashed_password = hash_password(password)
    create_user(username, hashed_password)

    return True