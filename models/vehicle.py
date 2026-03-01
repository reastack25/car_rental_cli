class Vehicle:
    def __init__(self, id, brand, cost_per_day):
        self.id = id
        self.brand = brand
        self.cost_per_day = cost_per_day

    def rental_cost(self,days):
        return self.cost_per_day * days
    