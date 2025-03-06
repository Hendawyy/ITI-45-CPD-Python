import hashlib
import json
import getpass
import ValidationFunctions as VF


def register_user():
    users_data = []

    try:
        with open('Users_Data.json', 'r') as file:
            users_data = json.load(file)
    except FileNotFoundError:
        with open('Users_Data.json', 'w') as file:
            json.dump(users_data, file)

    first_name = input("Enter your First Name: ")
    while not VF.validate_name(first_name):
        print("Invalid input. First name should not contain numbers or spaces or special characters.")
        first_name = input("Enter your First Name: ")

    last_name = input("Enter your Last Name: ")
    while not VF.validate_name(last_name):
        print("Invalid input. Last name should not contain numbers or spaces or special characters.")
        last_name = input("Enter your Last Name: ")

    email = input("Enter your Email: ")
    while not VF.validate_email(email):
        print("Invalid email format.\nEmail format must be : something@something.(TLD)")
        email = input("Enter your Email: ")
    existing_emails = [user['Email'] for user in users_data]
    while email in existing_emails:
        print("This email is already registered.")
        email = input("Please Enter your Email: ")

    password = getpass.getpass("Enter your Password: ")
    while not VF.validate_password(password):
        print("Invalid password format.")
        print("Password must be at least 8 characters long.")
        print("It should contain at least one number, lowercase letter, uppercase letter, and special character.")
        password = getpass.getpass("Enter your Password: ")

    confirm_password = getpass.getpass("Confirm your Password: ")
    while password != confirm_password:
        print("Passwords do not match.")
        confirm_password = getpass.getpass("Confirm your Password: ")

    hashed_password = hashlib.sha1(password.encode()).hexdigest()

    phone = input("Enter your Mobile Phone: ")
    while not VF.validate_phone(phone):
        print("Invalid phone number.")
        phone = input("Enter your Mobile Phone: ")
    existing_phones = [user['Mobile Phone'] for user in users_data]
    while phone in existing_phones:
        print("This Phone is already registered.")
        phone = input("Please Enter your Mobile Phone: ")

    user_data = {
        "First Name": first_name,
        "Last Name": last_name,
        "Email": email,
        "Password": hashed_password,
        "Mobile Phone": phone
    }

    # print(users_data)

    users_data.append(user_data)
    with open('Users_Data.json', 'w') as file:
        json.dump(users_data, file, indent=4)

    print("Registration successful!")