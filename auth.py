import database
from ui import print_text, Colors

def authenticate():
    while True:
        print_text("\n--- WELCOME TO THE CHRONICLES ---", Colors.CYAN)
        print("1. Register New Account")
        print("2. Login")
        print("3. Exit Game")
        choice = input("Select an option: ").strip()

        if choice == "3":
            return None

        if choice in ["1", "2"]:
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            
            if not username or not password:
                print_text("Username and password cannot be empty!", Colors.RED)
                continue

            user_record = database.find_user(username)

            if choice == "1":
                if user_record:
                    print_text("Username already taken!", Colors.RED)
                else:
                    player = database.create_user(username, password)
                    print_text("Registration successful! Account logged in.", Colors.GREEN)
                    return player
            elif choice == "2":
                if user_record and user_record["password"] == password:
                    print_text(f"Welcome back, {username}!", Colors.GREEN)
                    return user_record
                else:
                    print_text("Invalid username or password.", Colors.RED)
