tasks = []

def add_task(task):
    tasks.append({"task": task, "done": False})

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True

def show_tasks():
    for i, task in enumerate(tasks):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. {task['task']} [{status}]")


# Example
add_task("Write Python Portfolio")
add_task("Upload to GitHub")
complete_task(0)
show_tasks()
