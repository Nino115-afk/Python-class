users = {}

def register():
    print("\n--- REGISTER ---")
    email = input("Enter your email: ")
    
    if "@" not in email:
        print("Error")
        return
    
    password = input("Enter your password: ")
    
    users[email] = password
    print("Registered successfully")

def login():
    print("\n--- LOGIN ---")
    email = input("Enter your email: ")
    
    if "@" not in email:
        print("Error")
        return
    
    password = input("Enter your password: ")
    
    if email in users and users[email] == password:
        print("Login successful!")
    else:
        print("Wrong email or password")

def main_menu():
    while True:
        print("\n=== MENU ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose (1-3): ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

main_menu()