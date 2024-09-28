import os
import json
from datetime import datetime


def main():
    
    filename= 'task_manager.json'
    tasks= load_task(filename)

    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            save_tasks(filename, tasks)
            break
        else:
            print("Invalid choice! Please try again.")


def load_task(filename):
    # Load tasks from the file
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return []


def save_tasks(filename, tasks):
    # Save tasks to the file
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)



#this function will add the task
def add_task(tasks):
    # Add a new task
    name = input("Task Name: ")
    description = input("Task Description: ")
    priority = input("Priority (high/medium/low): ").lower()
    due_date = input("Due Date (YYYY-MM-DD): ")
    tasks.append({
        'name': name,
        'description': description,
        'priority': priority,
        'due_date': due_date,
        'status': 'incomplete'
    })

def view_tasks(tasks):
    # View tasks based on user's choice
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        print(f"{idx}. {task['name']} ({task['priority']}) - {task['status']}")

def mark_task_complete(tasks):
    # Mark a task as complete
    task_num = int(input("Enter task number to mark as complete: "))
    tasks[task_num - 1]['status'] = 'complete'



if __name__=="__main__":
    main()