from models.vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, id, brand, cost_per_day, load_capacity):
        super().__init__(id, brand, cost_per_day)
        self.load_capacity = load_capacity

    def truck_info(self):
        return f"{self.brand} of id {self.id} with a capacity of {self.load_capacity} tons costing {self.cost_per_day} per day"