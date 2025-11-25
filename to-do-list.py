# to_do_list.py

import os

TASKS_FILE = "tasks.txt"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks yet!")
    else:
        print("\n📋 Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            new_task = input("Enter new task: ")
            tasks.append(new_task)
            save_tasks(tasks)
            print("✅ Task added!")

        elif choice == "3":
            show_tasks(tasks)
            task_no = int(input("Enter task number to mark done: "))
            if 0 < task_no <= len(tasks):
                tasks[task_no - 1] += " ✔️"
                save_tasks(tasks)
                print("✅ Task marked as done!")
            else:
                print("❌ Invalid task number.")

        elif choice == "4":
            show_tasks(tasks)
            task_no = int(input("Enter task number to delete: "))
            if 0 < task_no <= len(tasks):
                tasks.pop(task_no - 1)
                save_tasks(tasks)
                print("🗑️ Task deleted!")
            else:
                print("❌ Invalid task number.")

        elif choice == "5":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()