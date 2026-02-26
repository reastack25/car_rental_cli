from utils.hasher import hash_password, verify_password
from models.user import User

class AuthService:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def register(self, username, password, role='customer'):
        if self.user_repo.find_user(username):
            return False, "Username already exists."
        password_hash = hash_password(password)
        user = User(username, password_hash, role)
        self.user_repo.add_user(user)
        return True, "User registered successfully."

    def authenticate(self, username, password):
        user = self.user_repo.find_user(username)
        if user and verify_password(password, user.password):
            return user
        return None

    def is_admin(self, user):
        return user and user.role == 'admin'