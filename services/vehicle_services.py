
class Car:
    def __init__(self, car_id, brand, model, price_per_day):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Rented"
        return f"[{self.car_id}] {self.brand} {self.model} - Ksh{self.price_per_day}/day - {status}"


class CarRentalService:
    def __init__(self):
        self.cars = []
        self.car_counter = 1


    def add_car(self, brand, model, price_per_day):
        car = Car(self.car_counter, brand, model, price_per_day)
        self.cars.append(car)
        self.car_counter += 1
        print("Car added successfully!\n")


    def view_cars(self):
        if not self.cars:
            print("No cars available.\n")
            return

        for car in self.cars:
            print(car)
        print()


    def view_available_cars(self):
        available = [car for car in self.cars if car.is_available]

        if not available:
            print("No available cars at the moment.\n")
            return

        for car in available:
            print(car)
        print()

  
    def rent_car(self, car_id, days):
        for car in self.cars:
            if car.car_id == car_id:
                if car.is_available:
                    car.is_available = False
                    total_cost = car.price_per_day * days
                    print(f"You rented {car.brand} {car.model}")
                    print(f"Total cost: ${total_cost}\n")
                    return
                else:
                    print("Car is already rented.\n")
                    return

        print("Car not found.\n")

    
    def return_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                if not car.is_available:
                    car.is_available = True
                    print("Car returned successfully!\n")
                    return
                else:
                    print("This car was not rented.\n")
                    return

        print("Car not found.\n")



class VehicleService:               
    def __init__(self, vehicle_repo, rental_repo):
        self.vehicle_repo = vehicle_repo
        self.rental_repo = rental_repo

    def add_vehicle(self,
                    type_: str,
                    brand: str,
                    cost_per_day: float,
                    seats: int | None = None,
                    engine_capacity: int | None = None,
                    load_capacity: float | None = None):
        
        record = {
            "type": type_,
            "brand": brand,
            "cost_per_day": cost_per_day,
            "seats": seats,
            "engine_capacity": engine_capacity,
            "load_capacity": load_capacity,
        }
        stored = self.vehicle_repo.add(record)     
        return True, stored

    def list_vehicles(self):
        return self.vehicle_repo.get_all()          



    service = CarRentalService()

    while True:
        print(" Car Rental System ")
        print("1. Add Car")
        print("2. View All Cars")
        print("3. View Available Cars")
        print("4. Rent Car")
        print("5. Return Car")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            price = float(input("Enter price per day: "))
            service.add_car(brand, model, price)

        elif choice == "2":
            service.view_cars()

        elif choice == "3":
            service.view_available_cars()

        elif choice == "4":
            car_id = int(input("Enter car ID: "))
            days = int(input("Number of rental days: "))
            service.rent_car(car_id, days)

        elif choice == "5":
            car_id = int(input("Enter car ID: "))
            service.return_car(car_id)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.\n")