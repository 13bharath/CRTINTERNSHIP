import json
from datetime import datetime

# Define the data file to store tasks
DATA_FILE = 'tasks.json'

# Initialize the task list
tasks = []

# Load tasks from the data file (if it exists)
try:
    with open(DATA_FILE, 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    pass

def save_tasks():
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task():
    title = input("Enter task title: ")
    priority = input("Enter task priority (high/medium/low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    
    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "completed": False
    }
    
    tasks.append(task)
    save_tasks()
    print(f"Task '{title}' added successfully!")

def remove_task():
    list_tasks()
    task_index = int(input("Enter the index of the task to remove: ")) - 1

    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks()
        print(f"Task '{removed_task['title']}' removed successfully!")
    else:
        print("Invalid task index.")

def mark_completed():
    list_tasks()
    task_index = int(input("Enter the index of the task to mark as completed: ")) - 1

    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks()
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def list_tasks():
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. Title: {task['title']} | Priority: {task['priority']} | Due Date: {task['due_date']} | Status: {status}")

while True:
    print("\nToDo List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Mark Task as Completed")
    print("4. List Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_task()
    elif choice == '2':
        remove_task()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        list_tasks()
    elif choice == '5':
        print("Exiting ToDo List Application.")
        break
    else:
        print("Invalid choice. Please try again.")
