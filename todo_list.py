from datetime import datetime

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):  # Adding tasks
        self.tasks.append({"task": task, "completed": False, "completed_at": None})
        print(f'Task "{task}" added.')

    def delete_task(self, task_number):  # Deleting tasks
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task["task"]}" deleted.')
        else:
            print("Invalid task number.")

    def complete_task(self, task_number):  # Mark a task as done
        if 0 < task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]
            if not task["completed"]:
                task["completed"] = True
                task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f'Task "{task["task"]}" marked as completed.')
            else:
                print(f'Task "{task["task"]}" is already completed.')
        else:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
            return

        print("\nTo-Do List:")
        for idx, task in enumerate(self.tasks, start=1):
            status = "✔" if task["completed"] else "✘"
            completed_at = f' (Completed at: {task["completed_at"]})' if task["completed"] else ""
            print(f"{idx}. {task['task']} [{status}]{completed_at}")
        print()
        
def main():
    todo_list = ToDoList()
    
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. View Tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to delete: "))
                todo_list.delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == "3":
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter the task number to mark as complete: "))
                todo_list.complete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
        elif choice == "4":
            todo_list.view_tasks()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()