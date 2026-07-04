# Simple To-Do List App

tasks = []

def show_tasks():
    if not tasks:
        print("\nNo tasks in the list.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        if tasks:
            try:
                task_num = int(input("Enter task number to remove: "))
                removed_task = tasks.pop(task_num - 1)
                print(f"Removed task: {removed_task}")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")