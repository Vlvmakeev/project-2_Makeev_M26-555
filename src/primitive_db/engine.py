import sys

import prompt


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