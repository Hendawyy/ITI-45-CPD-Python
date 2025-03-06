import hashlib
import json
from Projects import UserMenu as UM

def login_user():
    users_data = []

    try:
        with open('Users_Data.json', 'r') as file:
            users_data = json.load(file)
    except FileNotFoundError:
        print("No registered users.")
        return

    email = input("Enter your Email: ")
    password = input("Enter your Password: ")
    hashed_password = hashlib.sha1(password.encode()).hexdigest()

    for user in users_data:
        if user['Email'] == email and user['Password'] == hashed_password:
            print("Login successful!")
            UM(user)
            return
    print("Invalid email or password.")