from datetime import date


def greet_user():

    print("Hello! Welcome to your Study Buddy.")
    name = input("What is your name? ")
    print(f"Nice to meet you, {name} Let's get organized.")

if __name__ == "__main__":
    greet_user()

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


if __name__ == "__main__":
    task = []
    greet_user()
    add_task(tasks)
    display_task(tasks)

