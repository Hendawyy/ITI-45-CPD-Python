import json

def delete_project(user):
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
        print("No projects available for deleting.")
        return

    print("Select a project to delete:")
    for idx, project in enumerate(filtered_projects, start=1):
        print(f"{idx}. {project['Title']}")

    while True:
        try:
            selected_project_idx = int(input("Enter the number of the project to delete: ")) - 1
            if 0 <= selected_project_idx:
                if selected_project_idx < len(filtered_projects):
                    break
                else:
                    print("Invalid selection: Index exceeds the number of projects.")
            else:
                print("Invalid selection: Index must be non-negative.")

        except ValueError:
            print("Invalid input.")

    project_to_delete = filtered_projects[selected_project_idx]

    original_idx = projects_data.index(project_to_delete)

    deleted_project = projects_data.pop(original_idx)

    with open('Projects_Data.json', 'w') as file:
        json.dump(projects_data, file, indent=4)

    print(f"Project '{deleted_project['Title']}' deleted successfully!")
