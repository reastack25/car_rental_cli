from models.vehicle import Vehicle

class Motorbike(Vehicle):
    def __init__(self, brand, cost_per_day, engine_capacity):
        super().__init__(brand, cost_per_day)
        self.engine_capacity = engine_capacity

    def motorbike_info(self):
        return f"{self.brand} with {self.engine_capacity} cc costing {self.cost_per_day} per day"