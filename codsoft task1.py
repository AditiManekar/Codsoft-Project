import os

# Define a dictionary to store the to-do items
todo_list = {}

# Function to display the to-do list
def display_todo_list():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {todo_list[task]}")

# Function to add a new task to the to-do list
def add_task(task):
    todo_list[len(todo_list) + 1] = task
    print(f"'{task}' has been added to your to-do list.")

# Function to update a task in the to-do list
def update_task(task_index, new_task):
    if task_index in todo_list:
        todo_list[task_index] = new_task
        print(f"Task {task_index} has been updated.")
    else:
        print("Invalid task index.")

# Function to delete a task from the to-do list
def delete_task(task_index):
    if task_index in todo_list:
        del todo_list[task_index]
        print(f"Task {task_index} has been deleted.")
    else:
        print("Invalid task index.")

# Function to save the to-do list to a file
def save_to_file(filename):
    with open(filename, 'w') as f:
        for task_index, task in todo_list.items():
            f.write(f"{task_index}: {task}\n")

# Function to load the to-do list from a file
def load_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.strip().split(': ')
                task_index = int(parts[0])
                task_description = ': '.join(parts[1:])
                todo_list[task_index] = task_description

# Main loop
def main():
    filename = "todo.txt"
    load_from_file(filename)

    while True:
        print("\nOptions:")
        print("1. Display To-Do List")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_todo_list()
        elif choice == '2':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '3':
            display_todo_list()
            task_index = int(input("Enter the index of the task to update: "))
            new_task = input("Enter the new task description: ")
            update_task(task_index, new_task)
        elif choice == '4':
            display_todo_list()
            task_index = int(input("Enter the index of the task to delete: "))
            delete_task(task_index)
        elif choice == '5':
            save_to_file(filename)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
