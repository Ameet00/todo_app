import json,os

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE) as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def add_task(title):
    tasks = load_tasks()
    task = {"id":len(tasks) + 1,
            "title":title,
             "done":False}
    tasks.append(task)
    save_tasks(tasks)
    print("ADD")

def list_task():
    tasks = load_tasks()
    if not tasks:
        print("There is no tasks")
        return
    for t in tasks:
        status = "[x]" if t["done"] else "[]"
        print(f"{t['id']}.{status}.{t['title']}")

def complete_task(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print("Done")
            return
    print("Task not found")

def delete_task(task_id):
    tasks = load_tasks()
    new = [t for t in tasks if t["id"] != task_id]
    save_tasks(new)
    print("Delete")


import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI TO-DO app")
    sub = parser.add_subparsers(dest="command")

    p_add = sub.add_parser("Add",help="Add task")
    p_add.add_argument("title",help="title")

    sub.add_parser("List",help="Show the tasks")

    p_done = sub.add_parser("Done",help="Task is done")
    p_done.add_argument("id",type=int)

    p_del = sub.add_parser("Delete",help="Delete task")
    p_del.add_argument("id",type=int)

    args = parser.parse_args()

    if args.command == "Add": add_task(args.title)
    elif args.command == "List": list_task()
    elif args.command == "Done": complete_task(args.id)
    elif args.command == "Delete": delete_task(args.id)
    else : parser.print_help()

if __name__ == "__main__":
    main()

