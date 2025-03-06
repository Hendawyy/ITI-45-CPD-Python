from tabulate import tabulate
import json

def view_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        print("File not found.")
        return

    if not data:
        print("No data available.")
        return

    headers = data[0].keys()
    rows = [list(entry.values()) for entry in data]
    print(tabulate(rows, headers=headers, tablefmt='grid'))
