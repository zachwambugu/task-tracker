import sys
import json

# Task manager to store and manage tasks
tasks = []

# Function to display the menu
def show_menu():
    print("\nTask Manager CLI")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Update Task")
    print("4. Mark Task as In Progress")
    print("5. Mark Task as Completed")
    print("6. Exit")

# Function to add a task
def add_task():
    task_name = input("Enter task name: ")
    task = {"name": task_name, "status": "Pending"}
    tasks.append(task)
    print(f"Task '{task_name}' added successfully!")

# to save the tasks in a file
def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)
    print("Tasks saved successfully!")

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        print("Tasks loaded successfully!")
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []


# Function to list all tasks
def list_tasks():
    if not tasks:
        print("No tasks available.")
        return
    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']} - {task['status']}")

# Function to update a task
def update_task():
    list_tasks()
    if not tasks:
        return
    try:
        task_index = int(input("Enter task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            new_name = input("Enter new task name: ")
            tasks[task_index]["name"] = new_name
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to mark a task as in progress
def mark_task_in_progress():
    list_tasks()
    if not tasks:
        return
    try:
        task_index = int(input("Enter task number to mark as in progress: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["status"] = "In Progress"
            print("Task marked as in progress!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to mark a task as completed
def mark_task_completed():
    list_tasks()
    if not tasks:
        return
    try:
        task_index = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["status"] = "Completed"
            print("Task marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

    
# Main function to handle user input
def main():
    load_tasks()
    while True:
        show_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                list_tasks()
            elif choice == 3:
                update_task()
            elif choice == 4:
                mark_task_in_progress()
            elif choice == 5:
                mark_task_completed()
            elif choice == 6:
                save_tasks()
                print("Exiting... Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
