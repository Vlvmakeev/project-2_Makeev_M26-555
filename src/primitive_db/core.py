from .utils import load_metadata, save_metadata

def create_table(metadata, table_name, columns):

    valid_types = {"int", "str", "bool"}
    
    tables = metadata

    if table_name in tables:
        print(f"Ошибка: таблица {table_name} уже существует!")
        return None

    id_column = ("ID", "int")

    if id_column not in columns:
        all_columns = [id_column] + list(columns)
    else:
        all_columns = list(columns)

    for col_name, col_type in all_columns:
        if col_type not in valid_types:
            print(f"Ошибка: Недопустимый тип данных '{col_type}' для столбца '{col_name}'"
                  f"Разрешены только: {', '.join(valid_types)}")
            return None

    tables[table_name] = {
        "columns": all_columns
    }

    columns_string = ", ".join([f"{name}:{dtype}" for name, dtype in all_columns])
    print(f"Таблица '{table_name}' успешно создана со столбцами: {columns_string}")

    save_metadata("src/primitive_db/db_meta.json", tables)

    return load_metadata("src/primitive_db/db_meta.json")


def drop_table(metadata, table_name):
    tables = metadata
    if table_name not in tables:
        print(f"Ошибка: таблицы {table_name} не существует!")
        return None
    tables.pop(table_name)

    print(f"Таблица {table_name} успешно удалена.")

    save_metadata("src/primitive_db/db_meta.json", tables)

    return load_metadata("src/primitive_db/db_meta.json")


def list_tables(metadata):
    for key in metadata:
        print("-", key)


def insert(metadata, table_name, values):
    tables = metadata

    current_table = tables[table_name]
    current_table_columns = current_table["columns"]

    if table_name not in tables:
        print(f"Ошибка: таблица {table_name} не существует!")
        return None

    print(len(values))
    print(values)
    print(len(current_table_columns))
    print(current_table_columns)

    if len(values) != len(current_table_columns) - 1:
        print(f"Ошибка: количество переданных значений не соответствует количеству полей таблицы {table_name} !")
        return None
    
    current_table_columns.pop(0)
    value_count = 0
    
    for value in values:
        if not isinstance(value, current_table_columns[value_count][1]):
            f"Ошибка: тип данных переданного значения {value} "
            f"не соответствует ожидаемому типу {current_table_columns[value_count][1]} "
            f"поля {current_table_columns[value_count][0]} "
            f"таблицы {table_name} !"

    columns_val = [col[0] for col in current_table_columns]
    table_rows = load_metadata("src/primitive_db/data/users.json")
    id_count
    new_row = zip(columns_val, values)
    if table_rows == {}:
        id_count = 1
        rows = []
        rows.append(
            new_row
        )
    else:
        id_count = len(table_rows) + 1
        table_rows.append(new_row)

    
