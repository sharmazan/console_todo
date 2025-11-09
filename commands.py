from tools import clear, user_command


def add_task() -> str:
    clear()
    return input("Enter the task: ")


def view_tasks(tasks, indexes=False):
    clear()

    if tasks:
        print("The tasks list:")
        for i, task in enumerate(tasks):
            if indexes:
                print(f"{i}: {task}")
            else:
                print(f"- {task}")
    else:
        print("There is no tasks!")


def complete_task(tasks):
    clear()
    view_tasks(tasks, indexes=True)
    print()
    if tasks:
        print("Select a task to complete")
        n = user_command(len(tasks))
        tasks.pop(n)
