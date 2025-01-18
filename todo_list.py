class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):  # adding tasks
        self.tasks.append({"task": task, "completed": False})
        print(f'Task "{task}" added.')

    def delete_task(self, task_number):  # deleting tasks
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task["task"]}" deleted.')
        else:
            print("Invalid task number.")

    def complete_task(self, task_number):  # mark a task as done
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f'Task "{self.tasks[task_number - 1]["task"]}" marked as completed.')
        else:
            print("Invalid task number.")

    def edit_task(self, task_number, new_task):  # editing a task
        if 0 < task_number <= len(self.tasks):
            old_task = self.tasks[task_number - 1]["task"]
            self.tasks[task_number - 1]["task"] = new_task
            print(f'Task "{old_task}" updated to "{new_task}".')
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return

        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            print(f"{idx}. {task['task']} [{status}]")
        print()

def main():
    todo_list = ToDoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. Edit Task")
        print("5. View Tasks")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_number)
        elif choice == "3":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to mark as complete: "))
            todo_list.complete_task(task_number)
        elif choice == "4":
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to edit: "))
            new_task = input("Enter the new task description: ")
            todo_list.edit_task(task_number, new_task)
        elif choice == "5":
            todo_list.view_tasks()
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
