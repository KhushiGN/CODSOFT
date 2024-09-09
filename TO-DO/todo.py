import json
import os

FILE_NAME = 'todo_list.json'

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(task_description):
    tasks = load_tasks()
    tasks.append({"description": task_description, "done": False})
    save_tasks(tasks)
    print(f"Task '{task_description}' added.")

def list_tasks():
    tasks = load_tasks()
    for idx, task in enumerate(tasks):
        status = "Done" if task["done"] else "Not Done"
        print(f"{idx + 1}. {task['description']} - {status}")

def mark_task_done(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks[task_index]['done'] = True
        save_tasks(tasks)
        print(f"Task {task_index + 1} marked as done.")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task Done")
        print("4. Exit")

        choice = input("Choose an option: ")
        
        if choice == '1':
            description = input("Enter task description: ")
            add_task(description)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            task_index = int(input("Enter task number to mark as done: ")) - 1
            mark_task_done(task_index)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
