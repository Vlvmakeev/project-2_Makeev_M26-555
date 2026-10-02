import sys

import prompt

from .utils import load_metadata, save_metadata

from .parser import sql_parser

from . import core

tables_commands = {"create_table", "list_tables", "drop_table", "info"}
sql_commands = {"insert", "select", "update", "delete"}
system_commands = {"help", "exit"}
available_commands = tables_commands | sql_commands | system_commands
metadata = load_metadata("src/primitive_db/db_meta.json")

def welcome():
    print("Первая попытка запустить проект!")

    command = prompt.string("Введите команду: ")
    args = command.split()
    user_command_name = args[0]
    if len(args) > 1:
        user_command_param = args[1]

    if not command.strip():
        return

    if command.split()[0] in sql_commands:
        args = sql_parser(command, user_command_name)

    match user_command_name:
        case wrong_command if wrong_command not in available_commands:
            print(f"Функции {wrong_command} нет. Попробуйте снова.")
            return
        
        case "exit":
            sys.exit()
        
        case "help":
            print_help()
        
        case "create_table":
            table_name = args[1]
            columns = [tuple(col.split(':', 1)) for col in args[2:]]
            core.create_table(metadata, table_name, columns)
        
        case "drop_table":
            core.drop_table(metadata, user_command_param)
        
        case "list_tables":
            core.list_tables(metadata)

        case "insert":
            core.insert(metadata, args[0], args[1])
            print(load_metadata(f"src/primitive_db/data/{args[0]}.json"))

        case "info":
            core.info(metadata, args[1])

        case "select":
            table_data = load_metadata(f"src/primitive_db/data/{args[0]}.json")
            result = core.select(table_data, args[1])
            print(result)

        case "delete":
            table_data = load_metadata(f"src/primitive_db/data/{args[0]}.json")
            result = core.delete(table_data, args[1])
            save_metadata(f"src/primitive_db/data/{args[0]}.json", result)
            print(load_metadata(f"src/primitive_db/data/{args[0]}.json"))

        case "update":
            table_name = args[1]
            table_data = load_metadata(f"src/primitive_db/data/{args[0]}.json")
            result = core.update(metadata, table_name, args[0], args[1])
            print(result)


def print_help():
   
    print("\n***Процесс работы с таблицей***")
    print("Функции:")
    print("<command> create_table <имя_таблицы> <столбец1:тип> .. - создать таблицу")
    print("<command> list_tables - показать список всех таблиц")
    print("<command> drop_table <имя_таблицы> - удалить таблицу")
    
    print("\n***Операции с данными***")
    print("<command> insert into <имя_таблицы> values (<значение1>, <значение2>, ...) - создать запись.")
    print("<command> select from <имя_таблицы> where <столбец> = <значение> - прочитать записи по условию.")
    print("<command> select from <имя_таблицы> - прочитать все записи.")
    print("<command> update <имя_таблицы> set <столбец1> = <новое_значение1> where <столбец_условия> = <значение_условия> - обновить запись.")
    print("<command> delete from <имя_таблицы> where <столбец> = <значение> - удалить запись.")
    print("<command> info <имя_таблицы> - вывести информацию о таблице.")

    
    print("\nОбщие команды:")
    print("<command> exit - выход из программы")
    print("<command> help - справочная информация\n")


def run():
    while True:
        welcome()
