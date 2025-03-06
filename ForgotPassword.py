import hashlib
import json
import ValidationFunctions as VF
import getpass

def change_password():
    users_data = []

    try:
        with open('Users_Data.json', 'r') as file:
            users_data = json.load(file)
    except FileNotFoundError:
        print("No registered users.")
        return

    email = input("Enter your Email: ")
    phone = input("Enter your Mobile Phone: ")

    user_found = False
    for user in users_data:
        if user['Email'] == email and user['Mobile Phone'] == phone:
            Newpassword = getpass.getpass("Enter your new Password: ")
            while not VF.validate_password(Newpassword):
                print("Invalid password format.")
                print("Password must be at least 8 characters long.")
                print("It should contain at least one number, lowercase letter, uppercase letter, and special character.")
                Newpassword = getpass.getpass("Enter your new Password: ")

            Newconfirm_password = getpass.getpass("Confirm your new Password: ")
            while Newpassword != Newconfirm_password:
                print("Passwords do not match.")
                Newconfirm_password = getpass.getpass("Confirm your new Password: ")

            hashed_new_password = hashlib.sha1(Newpassword.encode()).hexdigest()
            user['Password'] = hashed_new_password
            with open('Users_Data.json', 'w') as file:
                json.dump(users_data, file, indent=4)
            print("Password changed successfully!")
            user_found = True
            break

    if not user_found:
        print("User not found or incorrect phone number.")

