import sys

import prompt

import shlex

from .utils import load_metadata, save_metadata

from . import core

tables_commands = {"create_table", "list_tables", "drop_table"}
sql_commands = {"insert", "select", "update", "delete", "info"}
system_commands = {"help", "exit"}
available_commands = {"create_table", "list_tables", "drop_table", "exit", "help", "insert"}
metadata = load_metadata("src/primitive_db/db_meta.json")

def welcome():
    print("Первая попытка запустить проект!")

    command = prompt.string("Введите команду: ")

    if not command.strip():
        return

    args = shlex.split(command)
    user_command = args[0]

    match user_command:
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
            core.drop_table(metadata, args[1])
        
        case "list_tables":
            core.list_tables(metadata)

        case "insert":
            core.insert(metadata, args[2], args[4])


def print_help():
    """Prints the help message for the current mode."""
   
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
