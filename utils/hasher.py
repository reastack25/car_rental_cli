import hashlib
import os

def hash_password(password):
    salt = os.urandom(16).hex()
    hash_obj = hashlib.sha256((password + salt).encode())
    return f"{salt}:{hash_obj.hexdigest()}"

def verify_password(password, password_hash):
    salt, stored_hash = password_hash.split(':')
    hash_obj = hashlib.sha256((password + salt).encode())
    return hash_obj.hexdigest() == stored_hash