from datetime import datetime  # Importing the datetime module to track task completion times

# Class to manage the to-do list
class ToDoList:
    def __init__(self):
        # Initialize the to-do list with an empty list to store tasks
        self.tasks = []

    # Method to add a new task
    def add_task(self, task):  
        # Add a task as a dictionary with default values for completion status and timestamp
        self.tasks.append({"task": task, "completed": False, "completed_at": None})
        print(f'Task "{task}" added.')

    # Method to delete a task by its number
    def delete_task(self, task_number):
        # Check if the given task number is valid
        if 0 < task_number <= len(self.tasks):
            # Remove the task from the list and notify the user
            removed_task = self.tasks.pop(task_number - 1)
            print(f'Task "{removed_task["task"]}" deleted.')
        else:
            print("Invalid task number.")  # Handle invalid input

    # Method to mark a task as completed
    def complete_task(self, task_number):
        # Check if the given task number is valid
        if 0 < task_number <= len(self.tasks):
            task = self.tasks[task_number - 1]  # Retrieve the task
            if not task["completed"]:  # Check if the task is not already completed
                # Update the task's status and set the completion timestamp
                task["completed"] = True
                task["completed_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f'Task "{task["task"]}" marked as completed.')
            else:
                print(f'Task "{task["task"]}" is already completed.')  # Notify if already completed
        else:
            print("Invalid task number.")  # Handle invalid input

    # Method to view all tasks in the list
    def view_tasks(self):
        # Check if there are no tasks in the list
        if not self.tasks:
            print("No tasks in the to-do list.")  # Notify if the list is empty
            return

        print("\nTo-Do List:")  # Header for the list display
        # Iterate through the tasks and display each with its status
        for idx, task in enumerate(self.tasks, start=1):
            # Show a checkmark (✔) for completed tasks and a cross (✘) for incomplete tasks
            status = "✔" if task["completed"] else "✘"
            # Include completion timestamp if the task is marked as completed
            completed_at = f' (Completed at: {task["completed_at"]})' if task["completed"] else ""
            print(f"{idx}. {task['task']} [{status}]{completed_at}")
        print()  # Add an empty line for better formatting
        
# Main function to interact with the to-do list
def main():
    todo_list = ToDoList()  # Create an instance of the ToDoList class
    
    while True:
        print("\nMenu:")
        print("1. Add Task") # Added a typo so that a colleague can fix a bug
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. View Tasks")
        print("5. Exit")
        
        choice = input("Choose an option: ")  # Prompt user for their choice

        if choice == "1":  # Option to add a task
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":  # Option to delete a task
            todo_list.view_tasks()  # Display tasks before deleting
            try:
                task_number = int(input("Enter the task number to delete: "))  # Get task number
                todo_list.delete_task(task_number)
            except ValueError:  # Handle non-integer input
                print("Invalid input. Please enter a valid task number.")
        elif choice == "3":  # Option to mark a task as complete
            todo_list.view_tasks()  # Display tasks before marking as complete
            try:
                task_number = int(input("Enter the task number to mark as complete: "))  # Get task number
                todo_list.complete_task(task_number)
            except ValueError:  # Handle non-integer input
                print("Invalid input. Please enter a valid task number.")
        elif choice == "4":  # Option to view tasks
            todo_list.view_tasks()
        elif choice == "5":  # Option to exit the program
            print("Exiting program. Goodbye!")
            break
        else:  # Handle invalid menu choices
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
