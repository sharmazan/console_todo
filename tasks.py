from tools import clear, user_command
from commands import add_task, view_tasks, complete_task

COMMANDS = [
    "1. Add task",
    "2. Complete task",
    "3. Edit task",
    "4. Delete task",
    "0. Exit",
]

tasks = []


def print_desc():
    for c in COMMANDS:
        print(c)


def print_hello():
    clear()
    print ("Hello in the Simple TODO App!")


def run():
    print_hello()
    print()
    view_tasks(tasks)
    print()
    print_desc()
    while True:
        n = user_command(len(COMMANDS))
        if n == 0:
            exit()
        elif n == 1:
            tasks.append(add_task())
            return
        elif n == 2:
            complete_task(tasks)
            return


if __name__ == "__main__":
    while True:
        run()


