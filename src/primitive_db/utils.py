import json

from prettytable import PrettyTable

def load_metadata(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_metadata(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def prettier_table(data):
    pretty_table = PrettyTable()
    pretty_table.field_names = [item[0] for item in data[0]]
    for row in data:
        row_values = [item[1] for item in row]
        pretty_table.add_row(row_values)
    print(pretty_table)
