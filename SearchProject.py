from datetime import datetime
import json
from tabulate import tabulate

def search_project():
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

    while True:
        search_date_str = input("Enter the date to search for (YYYY-MM-DD): ")
        try:
            search_date = datetime.strptime(search_date_str, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")

    FR = [project for project in projects_data if datetime.strptime(project['Start Date'], "%Y-%m-%d") == search_date]

    if not FR:
        print("No projects found matching the search criteria.")
        return

    headers = FR[0].keys()
    rows = [list(entry.values()) for entry in FR]
    print(tabulate(rows, headers=headers, tablefmt='grid'))

