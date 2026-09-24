import sys

import prompt

import shlex

from .utils import load_metadata, save_metadata

from . import core


def welcome():
    metadata = load_metadata("src/primitive_db/db_meta.json")

    print("Первая попытка запустить проект!")

    print("\n")

    command = ""

    command = prompt.string("Введите команду: ")

    if command != "":
        args = shlex.split(command)

    match args[0]:
        case "exit":
            sys.exit()
        case "help":
            print_help()
            command = prompt.string("Введите команду: ")
        case "create_table":
            table_name = args[1]
            columns = [tuple(col.split(':', 1)) for col in args[2:]]
            core.create_table(metadata, table_name, columns)
        case "drop_table":
            core.drop_table(metadata, args[1])
        case "list_tables":
            core.list_tables(metadata)
        case _:
            command = prompt.string("Введите команду: ")


def print_help():
    """Prints the help message for the current mode."""
   
    print("\n***Процесс работы с таблицей***")
    print("Функции:")
    print("<command> create_table <имя_таблицы> <столбец1:тип> .. - создать таблицу")
    print("<command> list_tables - показать список всех таблиц")
    print("<command> drop_table <имя_таблицы> - удалить таблицу")
    
    print("\nОбщие команды:")
    print("<command> exit - выход из программы")
    print("<command> help - справочная информация\n")


def run():
     pass
     while(True):
        load_metadata("src/primitive_db/db_meta.json")
        welcome()
