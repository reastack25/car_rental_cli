from models.vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, id, brand, cost_per_day, seats):
        super().__init__(id, brand, cost_per_day)
        self.seats = seats

    def car_info(self):
        return f"{self.brand} of id {self.id} with {self.seats} seats costing {self.cost_per_day} per day"