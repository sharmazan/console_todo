from tools import clear, user_command
from commands import add_task, view_tasks, complete_task
from storage import load_tasks, save_tasks

COMMANDS = [
    "1. Add task",
    "2. Complete task",
    "0. Exit",
]

TASKS_FILE = "tasks.txt"

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
            save_tasks(TASKS_FILE, tasks)
            exit()
        elif n == 1:
            tasks.append(add_task())
            return
        elif n == 2:
            complete_task(tasks)
            return


if __name__ == "__main__":
    load_tasks(TASKS_FILE, tasks)
    while True:
        run()
