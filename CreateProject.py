import json
from datetime import datetime

def create_project(user):
    projects_data = []

    try:
        with open('Projects_Data.json', 'r') as file:
            projects_data = json.load(file)
    except FileNotFoundError:
        with open('Projects_Data.json', 'w') as file:
            json.dump(projects_data, file)

    title = input("Enter project title: ")
    while not title.strip():
        print("Title cannot be empty.")
        title = input("Enter project title: ")

    details = input("Enter project details: ")
    while not details.strip():
        print("Details cannot be empty.")
        details = input("Enter project details: ")

    total_target = input("Enter total target amount (EGP): ")
    while not total_target or not total_target.isnumeric():
        print("Invalid input. Please enter a valid numeric amount for total target.")
        total_target = input("Enter total target amount (EGP): ")
    total_target = float(total_target)

    while True:
        start_date_str = input("Enter start date (YYYY-MM-DD): ")
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    while True:
        end_date_str = input("Enter end date (YYYY-MM-DD): ")
        try:
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            if end_date <= start_date:
                print("End date should be after the start date.")
            else:
                break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    project_data = {
        "Title": title,
        "Details": details,
        "Total Target": total_target,
        "Start Date": start_date_str,
        "End Date": end_date_str,
        "Project Owner": user["Mobile Phone"]
    }
    print(user["Mobile Phone"])
    projects_data.append(project_data)
    with open('Projects_Data.json', 'w') as file:
        json.dump(projects_data, file, indent=4)

    print("Project created successfully!")


