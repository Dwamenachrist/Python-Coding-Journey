from datetime import date


def greet_user():

    print("Hello! Welcome to your Study Buddy.")
    name = input("What is your name? ")
    print(f"Nice to meet you, {name} Let's get organized.")


# List of dictionaries to store information about tasks

tasks = [
    {
        "task": "Finish chapter 3 reading",
        "subject": "History",
        "due_date": date(2024, 12, 28),
        "priority": 2,
        "completed": False
    },
    {
        "task": "Work on coding assignment",
        "subject": "Coding",
        "due_date": date(2024, 12, 26),
        "priority": 1,
        "completed": False
    }
    # ... more tasks
]

def add_task(tasks):
    """ Adds a new task to the task list"""
    task = input("Enter task description ")
    subject = input("Enter subject: ")

    while True:
        try:
            year = int(input("Enter due date year (YYYY): "))
            month = int(input("Enter due date month (MM): "))
            day = int(input("Enter due date day(DD): "))
            due_date = date(year, month, day)
            break
        except ValueError:
            print("Invalid date format. Please try again.")


    while True:
        try:
            priority = int(input("Enter priority (1-3, 1 being highest): "))
            if 1 <= priority <= 3:
                break
            else:
                print("Priority must be between 1 and 3. Please try again.")
        except ValueError:
            print("Invalid priority. Please enter an integer.")
    tasks.append({
        "task": task,
        "subject": subject,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    })
    print("Task added successfully.")


def display_task(tasks):
    """ Displays all the tasks in the tasks list in a formatted way"""

    if not tasks:
        print("No tasks added! Add some tasks to get started.")
        return

    for i, task in enumerate(tasks):
        status = "√" if task["completed"] else "✗"
        print(f"Task {i+1}: {task['task']} {status}")
        print(f"Task {i+1} [{status}] {task['task']} ({task['subject']}) - Due: {task['due_date']} - Priority: {task['priority']}")




def mark_task_complete(tasks):
  """Marks a task as complete."""

  display_task(tasks)  # Show tasks with their numbers

  while True:
    try:
      task_number = int(input("Enter the number of the task to mark complete: ")) - 1
      if 0 <= task_number < len(tasks):
        tasks[task_number]["completed"] = True
        print("Task marked as complete!")
        break
      else:
        print("Invalid task number. Please try again.")
    except ValueError:
      print("Invalid input. Please enter a number.")



def sort_tasks(tasks):
  """Sorts tasks by due date and then by priority."""

  tasks.sort(key=lambda task: (task["due_date"], task["priority"]))
  print("Tasks sorted!")


def main():
  """Main function to run the study planner."""

  tasks = []
  greet_user()

  while True:
    print("\nChoose an action:")
    print("1. Add task")
    print("2. Display tasks")
    print("3. Mark task complete")
    print("4. Sort tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
      add_task(tasks)
    elif choice == '2':
      display_tasks(tasks)
    elif choice == '3':
      mark_task_complete(tasks)
    elif choice == '4':
      sort_tasks(tasks)
    elif choice == '5':
      print("Exiting Study Buddy. Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()