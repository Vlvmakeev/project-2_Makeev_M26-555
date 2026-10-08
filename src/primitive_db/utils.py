import json

from prettytable import PrettyTable


def load_metadata(filepath):
    """Загружает содержимое файла по пути
    Args:
        filepath (str): Путь к файлу, строка.
    Returns:
        json.load: Содержимое файла.
        {} при ошибке
    Raises:
        FileNotFoundError: Если файл не найден.
        json.JSONDecodeError: При ошибке десериализации.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data if data is not None else {}
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_metadata(filepath, data):
    """Сохраняет данные в файл по пути
    Args:
        filepath (str): Путь к файлу, строка.
        data(object): данные для сохранения, в формале list
    Returns:
        None
    Raises:
        FileNotFoundError: Если файл не найден.
        json.JSONDecodeError: При ошибке десериализации.
    """
    if data is None:
        print("Ошибка: нечего сохранять (data is None).")
        return
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Ошибка: файл не найден!")

def load_table_data(table_name):
    """Загружает данные таблицы по пути файла
    Args:
        table_name (str): Путь к файлу, строка.
    Returns:
        json.load: Содержимое файла.
        {} при ошибке
    Raises:
        FileNotFoundError: Если файл не найден.
        json.JSONDecodeError: При ошибке десериализации.
    """
    return load_metadata(f"src/primitive_db/data/{table_name}.json")

def save_table_data(table_name, data):
    """Сохраняет данные таблицы по пути файла
    Args:
        table_name (str): Путь к файлу, строка.
        data(object): данные для сохранения, в формале list
    Returns:
        None
    Raises:
        FileNotFoundError: Если файл не найден.
        json.JSONDecodeError: При ошибке десериализации.
    """
    save_metadata(f"src/primitive_db/data/{table_name}.json", data)

def prettier_table(data):
    """Форматирует данные через PrettyTable, выводит через print
    Args:
        data(object): данные для форматирования, в формале list
    Returns:
        None
    """

    if not data:
        print("Нет данных для отображения.")
        return

    first_row = data[0]
    if not isinstance(first_row, list) or not first_row:
        print("Нат данных для отображения.")
        return

    pretty_table = PrettyTable()
    pretty_table.field_names = [item[0] for item in data[0]]
    for row in data:
        row_values = [item[1] for item in row]
        pretty_table.add_row(row_values)
    print(pretty_table)
