import json
import os

class DatabaseManager:
    def __init__(self,filename= "database.json"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({"users": [], "vehicles": [], "rentals": []}, f)

    def load(self):
        with open(self.filename, "r") as f:
            return json.load(f)
        
    def save(self,data):
        with open(self.filename, "w") as f:
            json.dump(data,f)