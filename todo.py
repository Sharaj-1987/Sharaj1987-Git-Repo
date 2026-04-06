import json
import os

DATA_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"Added: {description}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, 1):
        status = "x" if task["done"] else " "
        print(f"  {i}. [{status}] {task['description']}")


def mark_done(number):
    tasks = load_tasks()
    if number < 1 or number > len(tasks):
        print(f"No task #{number}.")
        return
    tasks[number - 1]["done"] = True
    save_tasks(tasks)
    print(f"Marked done: {tasks[number - 1]['description']}")


def print_help():
    print("Usage:")
    print("  python todo.py add <task>     Add a new task")
    print("  python todo.py list           List all tasks")
    print("  python todo.py done <number>  Mark a task as done")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print_help()
    elif sys.argv[1] == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "done" and len(sys.argv) > 2:
        try:
            mark_done(int(sys.argv[2]))
        except ValueError:
            print("Please provide a valid task number.")
    else:
        print_help()
