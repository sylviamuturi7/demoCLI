#!/usr/bin/env python3

from utils import load_data, save_data

class Person:
    total_people = 0
    
    def __init__(self, name):
        self.name = name
        Person.total_people += 1
    
    def __str__(self):
        return f"Person: {self.name}"

class User(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email
        self.projects = []
        self._id = Person.total_people
    
    @property
    def user_id(self):
        return self._id
    
    @user_id.setter
    def user_id(self, value):
        if isinstance(value, int) and value > 0:
            self._id = value
    
    def __str__(self):
        return f"User({self.user_id}): {self.name} - {self.email}"
    
    def __repr__(self):
        return f"User(name='{self.name}', email='{self.email}')"
    
    def to_dict(self):
        return {"name": self.name, "email": self.email, "projects": self.projects, "id": self._id}
    
    @classmethod
    def from_dict(cls, data):
        user = User(data["name"], data["email"])
        user.projects = data.get("projects", [])
        user._id = data.get("id", 0)
        return user

class Project:
    total_projects = 0
    
    def __init__(self, title, description, due_date, user_name):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.user_name = user_name
        self.tasks = []
        self._id = Project.total_projects + 1
        Project.total_projects += 1
    
    @property
    def project_id(self):
        return self._id
    
    def __str__(self):
        return f"Project({self.project_id}): {self.title} (Due: {self.due_date})"
    
    def __repr__(self):
        return f"Project(title='{self.title}', user='{self.user_name}')"
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date,
            "user_name": self.user_name,
            "tasks": self.tasks,
            "id": self._id
        }
    
    @classmethod
    def from_dict(cls, data):
        project = Project(data["title"], data["description"], data["due_date"], data["user_name"])
        project.tasks = data.get("tasks", [])
        project._id = data.get("id", 0)
        return project

class Task:
    total_tasks = 0
    
    def __init__(self, title, status, assigned_to, project_title):
        self.title = title
        self.status = status
        self.assigned_to = assigned_to
        self.project_title = project_title
        self._id = Task.total_tasks + 1
        Task.total_tasks += 1
    
    @property
    def task_id(self):
        return self._id
    
    def __str__(self):
        return f"Task({self.task_id}): {self.title} [{self.status}] - {self.assigned_to}"
    
    def __repr__(self):
        return f"Task(title='{self.title}', status='{self.status}')"
    
    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to,
            "project_title": self.project_title,
            "id": self._id
        }
    
    @classmethod
    def from_dict(cls, data):
        task = Task(data["title"], data["status"], data["assigned_to"], data["project_title"])
        task._id = data.get("id", 0)
        return task

class ProjectManager:
    def __init__(self):
        self.data = load_data()
        self.users = {}
        for name, data in self.data["users"].items():
            self.users[name] = User.from_dict(data)
        
        self.projects = {}
        for title, data in self.data["projects"].items():
            self.projects[title] = Project.from_dict(data)
        
        self.tasks = {}
        for title, data in self.data["tasks"].items():
            self.tasks[title] = Task.from_dict(data)
    
    def save(self):
        self.data["users"] = {}
        for name, user in self.users.items():
            self.data["users"][name] = user.to_dict()
        
        self.data["projects"] = {}
        for title, project in self.projects.items():
            self.data["projects"][title] = project.to_dict()
        
        self.data["tasks"] = {}
        for title, task in self.tasks.items():
            self.data["tasks"][title] = task.to_dict()
        
        save_data(self.data)
    
    def add_user(self, name, email):
        if name in self.users:
            return False
        self.users[name] = User(name, email)
        self.save()
        return True
    
    def add_project(self, title, description, due_date, user_name):
        if title in self.projects or user_name not in self.users:
            return False
        project = Project(title, description, due_date, user_name)
        self.projects[title] = project
        self.users[user_name].projects.append(title)
        self.save()
        return True
    
    def add_task(self, title, status, assigned_to, project_title):
        if title in self.tasks or project_title not in self.projects:
            return False
        task = Task(title, status, assigned_to, project_title)
        self.tasks[title] = task
        self.projects[project_title].tasks.append(title)
        self.save()
        return True
    
    def update_task_status(self, title, new_status):
        if title not in self.tasks:
            return False
        self.tasks[title].status = new_status
        self.save()
        return True
    
    def list_users(self):
        return list(self.users.keys())
    
    def list_user_projects(self, user_name):
        if user_name not in self.users:
            return []
        return self.users[user_name].projects
    
    def list_project_tasks(self, project_title):
        if project_title not in self.projects:
            return []
        tasks = []
        for task_title in self.projects[project_title].tasks:
            if task_title in self.tasks:
                task = self.tasks[task_title]
                tasks.append({
                    "title": task.title,
                    "status": task.status,
                    "assigned_to": task.assigned_to
                })
        return tasks
