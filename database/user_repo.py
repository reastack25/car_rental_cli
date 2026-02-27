from db_manager import DatabaseManager

class UserRepo:
    def __init__(self):
        self.db = DatabaseManager()

    def add_user(self,user):
        data = self.db.load()
        data["users"].append(user.__dict__)
        self.db.save(data)

    def find_user(self, username):
        data = self.db.load()
        for user in data["users"]:
            if user["username"] == username:
                return user
        return None
    
    def get_all(self):
        return self.db.load()["users"]
        
        