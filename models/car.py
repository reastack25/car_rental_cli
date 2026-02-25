from models.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, cost_per_day, seats):
        super().__init__(brand, cost_per_day)
        self.seats = seats

    def car_info(self):
        return f"{self.brand} with {self.seats} seats costing {self.cost_per_day} per day"