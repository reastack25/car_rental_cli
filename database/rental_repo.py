from db_manager import DatabaseManager

class RentalRepo:
    def __init__(self):
        self.db = DatabaseManager()

    def add_rental(self,rental):
        data = self.db.load()
        data["rentals"].append(rental.__dict__)
        self.db.save(data)

    def get_all(self):
        return self.db.load()["rentals"]