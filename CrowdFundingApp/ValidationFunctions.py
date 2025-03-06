import re

def validate_name(name):
    return name.strip() and name.isalpha() and not any(char.isdigit() or not char.isalpha() for char in name)


def validate_email(email):
    email_pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_pattern, email)

def validate_password(password):
    password_pattern = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=!]).{8,}$'
    return re.match(password_pattern, password)


def validate_phone(phone):
    phone_pattern = r'^01[0-9]{9}$'
    return re.match(phone_pattern, phone)


