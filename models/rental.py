class Rental:
    def __init__(self,user,vehicle,days):
        self.user = user
        self.vehicle = vehicle
        self.days = days
        self.total_cost = vehicle.rental_cost(days)