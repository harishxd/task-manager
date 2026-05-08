# task_backend.py

tasks = []

def add_task(task):
    if task:
        tasks.append(task)
        return True
    return False

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        return True
    return False

def update_task(old, new):
    if old in tasks:
        ind = tasks.index(old)
        tasks[ind] = new
        return True
    return False

def get_tasks():
    return tasks