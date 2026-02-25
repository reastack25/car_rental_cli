from db_manager import DatabaseManager

class VehicleRepo:
    def __init__(self):
        self.db = DatabaseManager()
        

    def add_vehicle(self,vehicle):
        data = self.db.load()
        data["vehicles"].append(vehicle.__dict__)
        self.db.sava(data)
        
    def get_all(self):
        return self.db.load()["vehicles"]
    