from datetime import datetime


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
        "due_date": datetime.date(2024, 12, 28),
        "priority": 2,
        "completed": False
    },
    {
        "task": "Work on coding assignment",
        "subject": "Coding",
        "due_date": datetime.date(2024, 12, 26),
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
            due_date = datetime.date(year, month, day)
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
    task.append({
        "task": task,
        "subject": subject,
        "due_date": due_date,
        "priority": priority,
        "completed": False
    })
    print("Task added successfully.")