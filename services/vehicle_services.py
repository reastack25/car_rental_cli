class Car:
    def __init__(self, car_id, brand, model, price_per_day):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Rented"
        return f"[{self.car_id}] {self.brand} {self.model} - ${self.price_per_day}/day - {status}"


class vehicleServices:
    def __init__(self):
        self.cars = []
        self.car_counter = 1

    # Add new car
    def add_car(self, brand, model, price_per_day):
        car = Car(self.car_counter, brand, model, price_per_day)
        self.cars.append(car)
        self.car_counter += 1
        print("Car added successfully!\n")

    # View all cars
    def view_cars(self):
        if not self.cars:
            print("No cars available.\n")
            return

        for car in self.cars:
            print(car)
        print() 

    # View only available cars
    def view_available_cars(self):
        available = [car for car in self.cars if car.is_available]  #LIST COMPREHENTION #looks at each car in the car list and checks if the car is available. If it is, it adds it to the available list.
        if not available:
            print("No available cars at the moment.\n")
            return

        for car in available:
            print(car)
        print()