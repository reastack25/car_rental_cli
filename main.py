#!/usr/bin/env python3
import argparse
import sys
import os
from database.user_repo import UserRepo
from database.vehicle_repo import VehicleRepo
from database.rental_repo import RentalRepo
from services.Auth_service import AuthService
from services.vehicle_services import VehicleServices
from services.rental_services import RentalService

def data_dir():
    if not os.path.exists('data'):
        os.makedirs('data')

def main():
    data_dir()
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    user_repo = UserRepo()
    vehicle_repo = VehicleRepo()
    rental_repo = RentalRepo()
    auth_service = AuthService(user_repo)
    vehicle_service = VehicleServices(vehicle_repo, rental_repo)
    rental_service = RentalService(rental_repo, vehicle_service, user_repo)

    parser = argparse.ArgumentParser(description="Car Rental CLI")
    subparsers = parser.add_subparsers(dest='command', help='Commands')


    reg_parser = subparsers.add_parser('register', help='Register a new user')
    reg_parser.add_argument('username')
    reg_parser.add_argument('password')
    reg_parser.add_argument('--role', choices=['customer', 'admin'], default='customer',
                            help='Role (default: customer)')

    
    args = parser.parse_args()
    if args.command == 'register':
        success, msg = auth_service.register(args.username, args.password, args.role)
        print(msg)
        sys.exit(0)
    elif args.command is None:
        pass
    else:
        
        print("You must be logged in.")
        sys.exit(1)

    
    print(" Car Rental System Login ")
    username = input("Username: ")
    password = input("Password: ")
    success, msg = auth_service.login(username, password)
    if not success:
        print(msg)
        sys.exit(1)
    print(msg)
    user = auth_service.get_current_user()

    
    parser2 = argparse.ArgumentParser(description="Car Rental CLI (logged in)")
    subparsers2 = parser2.add_subparsers(dest='command', required=True)

    
    add_vehicle_parser = subparsers2.add_parser('add-vehicle', help='Add a vehicle (admin only)')
    add_vehicle_parser.add_argument('type', choices=['car', 'motorbike', 'truck'])
    add_vehicle_parser.add_argument('brand')
    add_vehicle_parser.add_argument('cost_per_day', type=float)
    add_vehicle_parser.add_argument('--seats', type=int, help='For car')
    add_vehicle_parser.add_argument('--engine-capacity', type=int, help='For motorbike')
    add_vehicle_parser.add_argument('--load-capacity', type=float, help='For truck')

    list_vehicles_parser = subparsers2.add_parser('list-vehicles', help='List all vehicles')

    
    rent_parser = subparsers2.add_parser('rent', help='Rent a vehicle')
    rent_parser.add_argument('vehicle_id', type=int)
    rent_parser.add_argument('days', type=int)

    return_parser = subparsers2.add_parser('return', help='Return a vehicle')
    return_parser.add_argument('rental_id', type=int)

    my_rentals_parser = subparsers2.add_parser('my-rentals', help='View your rentals')

    
    list_users_parser = subparsers2.add_parser('list-users', help='List all users (admin only)')
    add_user_parser = subparsers2.add_parser('add-user', help='Add a new user (admin only)')
    add_user_parser.add_argument('username')
    add_user_parser.add_argument('password')
    add_user_parser.add_argument('--role', choices=['customer', 'admin'], default='customer')

    list_all_rentals_parser = subparsers2.add_parser('list-all-rentals', help='View all rentals (admin only)')

    logout_parser = subparsers2.add_parser('logout', help='Log out')

    args2 = parser2.parse_args(sys.argv[1:] if len(sys.argv) > 1 else [])

    
if __name__ == '__main__':
    main()
