from datetime import datetime


class User:
    def __init__(self, username):
        self.username = username
        self.projects = []

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "username": self.username,
            "projects": [project.to_dict() for project in self.projects]
        }


class Project:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "tasks": [task.to_dict() for task in self.tasks]
        }


class Task:
    def __init__(self, title, contributor):
        self.title = title
        self.contributor = contributor
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def mark_complete(self):
        self.completed = True

    def to_dict(self):
        return {
            "title": self.title,
            "contributor": self.contributor,
            "completed": self.completed,
            "created_at": self.created_at
        }