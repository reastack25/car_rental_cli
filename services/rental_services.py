from services.vehicle_services import *



class Car:
    def __init__(self, car_id, brand, model, price_per_day):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.is_available = True

class CarRentalService:
    def __init__(self):
        self.cars = []
        self.car_counter = 1

    # Rent a car
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




    # Return a car
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


# menu inside the file
# if __name__ == "__main__":
service = CarRentalService()

while True:
        print("=== Car Rental System ===")
        print("1. Add Car")
        print("2. View All Cars")
        print("3. View Available Cars")         # Options
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