from utils import load_metadata

def create_table(metadata, table_name, columns):

    valid_types = {"int", "str", "bool"}
    
    tables = load_metadata(metadata)

    if table_name in tables:
        print("Ошибка: таблица {table_name} уже существует!")
        return None

    id_column = ("ID", "int")
    all_columns = [id_column] + list(columns)

    for col_name, col_type in all_columns:
        if col_type not in valid_types:
            print(f"Ошибка: Недопустимый тип данных '{col_type}' для столбца '{col_name}'"
                  f"Разрешены только: {', '.join(valid_types)}")
            return None

def drop_table(metadata, table_name):
    pass

def list_tables():
    pass