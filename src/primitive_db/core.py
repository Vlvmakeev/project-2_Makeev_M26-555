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