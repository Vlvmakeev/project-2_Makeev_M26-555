import sys

import prompt

import shlex


def welcome():
    print("Первая попытка запустить проект!")

    print("\n")

    command = ""

    command = prompt.string("Введите команду: ")

    if command == "exit":
        sys.exit()
    elif command == "help":
            print("***")
            print("<command> exit - выйти из программы")
            print("<command> help - справочная информация")
            command = prompt.string("Введите команду: ")
    else:
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