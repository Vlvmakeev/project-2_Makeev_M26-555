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

    if table_name not in tables:
            print(f"Ошибка: таблица {table_name} не существует!")
            return None

    current_table = tables[table_name]
    current_table_columns = [
        col for col in current_table["columns"] if col[0].lower() != "id"
    ]

    if len(values) != len(current_table_columns):
        print(f"Ошибка: количество переданных значений не соответствует количеству полей таблицы {table_name} !")
        print(len(values))
        print(values)
        print(len(current_table_columns))
        print(current_table_columns)
        return None
    
    value_count = 0


    TYPE_MAP = {
    "int": int,
    "str": str,
    "bool": bool,
}
    
    for value in values:
        expected_type = TYPE_MAP[current_table_columns[value_count][1]]
        if not isinstance(value, expected_type):
            print(
                f"Ошибка: тип данных переданного значения {value} "
                f"не соответствует ожидаемому типу {current_table_columns[value_count][1]} "
                f"поля {current_table_columns[value_count][0]} "
                f"таблицы {table_name} !"
            )
        value_count += 1

    columns_val = [col[0] for col in current_table_columns]
    table_rows = load_metadata("src/primitive_db/data/users.json")
    id_count = 0
    new_row = [[col, value] for col, value in zip(columns_val, values)]
    if table_rows == {}:
        id_count = 1
        table_rows = []
        new_row.insert(0, ['ID', id_count])
        table_rows.append(
            new_row
        )
    else:
        id_count = len(table_rows) + 1
        new_row.insert(0,  ['ID', id_count])
        table_rows.append(new_row)

    save_metadata("src/primitive_db/data/users.json", table_rows)
