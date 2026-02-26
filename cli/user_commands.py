def handle_register(args, auth_service):
    success, msg = auth_service.register(args.username, args.password, args.role)
    print(msg)

def handle_add_user(args, auth_service):
    admin = auth_service.authenticate(args.username, args.password)
    if not admin:
        print("Invalid credentials.")
        return
    if not auth_service.is_admin(admin):
        print("Admin privileges required.")
        return
    success, msg = auth_service.register(args.new_username, args.new_password, args.role)
    print(msg)

def handle_list_users(args, auth_service):
    admin = auth_service.authenticate(args.username, args.password)
    if not admin or not auth_service.is_admin(admin):
        print("Admin credentials required.")
        return
    users = auth_service.user_repo.get_all()
    if not users:
        print("No users found.")
        return
    for u in users:
        print(f"  {u}")