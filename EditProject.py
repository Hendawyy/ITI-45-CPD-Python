from datetime import datetime
import json

def edit_projects(user):
    projects_data = []

    try:
        with open('Projects_Data.json', 'r') as file:
            projects_data = json.load(file)
    except FileNotFoundError:
        print("No projects available.")
        return

    if not projects_data:
        print("No projects available.")
        return

    filtered_projects = [project for project in projects_data if project['Project Owner'] == user['Mobile Phone']]

    if not filtered_projects:
        print("No projects available for editing.")
        return

    print("Select a project to edit:")
    for idx, project in enumerate(filtered_projects, start=1):
        if idx == 6:
            continue
        print(f"{idx}. {project['Title']}")

    while True:
        try:
            selected_project_idx = int(input("Enter the number of the project to edit: ")) - 1
            selected_project = filtered_projects[selected_project_idx]
            break
        except (ValueError, IndexError):
            print("Invalid selection.")

    print("Select a field to edit:")
    field_keys = list(selected_project.keys())
    for idx, key in enumerate(field_keys, start=1):
        if idx == 6:
            continue
        else:
            print(f"{idx}. {key}")

    while True:
        try:
            selected_field_idx = int(input("Enter the number of the field to edit: ")) - 1
            selected_field = field_keys[selected_field_idx]
            if selected_field == "Project Owner":
                print("Invalid selection.")
                continue
            else:
                break
        except (ValueError, IndexError):
            print("Invalid selection.")

    while True:
        new_value = input(f"Enter new value for {selected_field}: ")

        if selected_field in ["Title", "Details"]:
            if not new_value.strip():
                print(f"{selected_field} cannot be empty.")
            else:
                break
        elif selected_field == "Total Target":
            if not new_value or not new_value.isnumeric():
                print("Invalid input. Please enter a valid numeric amount for total target.")
            else:
                new_value = float(new_value)
                break
        elif selected_field in ["Start Date", "End Date"]:
            try:
                new_date = datetime.strptime(new_value, "%Y-%m-%d")
                if selected_field == "End Date" and new_date <= datetime.strptime(selected_project["Start Date"], "%Y-%m-%d"):
                    print("End date should be after the start date.")
                else:
                    break
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")

    selected_project[selected_field] = new_value

    with open('Projects_Data.json', 'w') as file:
        json.dump(projects_data, file, indent=4)

    print("Project updated successfully!")

