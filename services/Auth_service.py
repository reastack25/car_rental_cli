from models.user import User

class AuthService:
    def __init__(self, user_repo):
        self.user_repo = user_repo
        self.current_user = None

    def register(self, username, password, role='customer'):
        if self.user_repo.find_by_username(username):
            return False, "Username already exists."
        user = User(username, password, role)
        self.user_repo.add_user(user)
        return True, f"User '{username}' registered successfully as {role}."

    def login(self, username, password):
        user = self.user_repo.find_by_username(username)
        if user and user.password == password:
            self.current_user = user
            return True, f"Welcome, {user.username}!"
        return False, "Invalid username or password."

    def logout(self):
        self.current_user = None
        return "Logged out."

    def get_current_user(self):
        return self.current_user

    def is_admin(self):
        return self.current_user and self.current_user.role == 'admin'