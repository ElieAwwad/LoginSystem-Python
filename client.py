import requests


while True:

    print("\n======================")
    print("      LOGIN SYSTEM")
    print("======================")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("======================")

    choice = input("Choose: ")

    if choice == "3":
        print("Goodbye!")
        break

    if choice != "1" and choice != "2":
        print("Invalid choice")
        continue

    username = input("Username: ")
    password = input("Password: ")

    if choice == "1":
        action = "register"
    else:
        action = "login"

    response = requests.post(
        "http://127.0.0.1:5000/auth",
        json={
            "action": action,
            "username": username,
            "password": password
        }
    )

    print("\nServer response:")
    print(response.json())