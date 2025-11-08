import os


def clear():
    os.system('cls' if os.name=='nt' else 'clear')


def user_command(max_number):
    n = ""
    available_commands = list(range(max_number))
    while (n not in available_commands):
        try:
            n = int(input("\n#: "))
        except ValueError:
            print("Enter the number!")
    return n
