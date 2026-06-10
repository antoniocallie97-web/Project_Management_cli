from models import User, Project, Task
from storage import save_data, load_data
from utils import print_table

users = []


def create_user():
    username = input("Enter username: ")

    user = User(username)
    users.append(user)

    print("User created successfully.")


def list_users():
    if not users:
        print("No users found.")
        return

    data = []

    for index, user in enumerate(users, start=1):
        data.append([index, user.username])

    print_table(data, ["ID", "Username"])


def add_project():
    username = input("Enter username: ")

    user = next((u for u in users if u.username == username), None)

    if not user:
        print("User not found.")
        return

    name = input("Project name: ")
    description = input("Description: ")

    project = Project(name, description)
    user.add_project(project)

    print("Project added successfully.")


def view_projects():
    username = input("Enter username: ")

    user = next((u for u in users if u.username == username), None)

    if not user:
        print("User not found.")
        return

    if not user.projects:
        print("No projects found.")
        return

    data = []

    for project in user.projects:
        data.append([project.name, project.description])

    print_table(data, ["Project", "Description"])


def add_task():
    username = input("Enter username: ")

    user = next((u for u in users if u.username == username), None)

    if not user:
        print("User not found.")
        return

    project_name = input("Project name: ")

    project = next(
        (p for p in user.projects if p.name == project_name),
        None
    )

    if not project:
        print("Project not found.")
        return

    title = input("Task title: ")
    contributor = input("Contributor: ")

    task = Task(title, contributor)

    project.add_task(task)

    print("Task added successfully.")


def mark_task_complete():
    username = input("Enter username: ")

    user = next((u for u in users if u.username == username), None)

    if not user:
        print("User not found.")
        return

    project_name = input("Project name: ")

    project = next(
        (p for p in user.projects if p.name == project_name),
        None
    )

    if not project:
        print("Project not found.")
        return

    task_title = input("Task title: ")

    for task in project.tasks:
        if task.title == task_title:
            task.mark_complete()
            print("Task completed.")
            return

    print("Task not found.")


def save():
    save_data(users)
    print("Data saved successfully.")


def menu():
    while True:
        print("\nPROJECT MANAGEMENT SYSTEM")
        print("1. Create User")
        print("2. List Users")
        print("3. Add Project")
        print("4. View Projects")
        print("5. Add Task")
        print("6. Complete Task")
        print("7. Save Data")
        print("8. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_user()

        elif choice == "2":
            list_users()

        elif choice == "3":
            add_project()

        elif choice == "4":
            view_projects()

        elif choice == "5":
            add_task()

        elif choice == "6":
            mark_task_complete()

        elif choice == "7":
            save()

        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()