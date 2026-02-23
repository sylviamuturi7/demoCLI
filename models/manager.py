#!/usr/bin/env python3

from typing import List, Dict, Any
from models.user import User
from models.project import Project
from models.task import Task
from utils.helpers import load_users, save_users, load_projects, save_projects, load_tasks, save_tasks

class ProjectManager:
    def __init__(self):
        self.users = {name: User.from_dict(data) for name, data in load_users().items()}
        self.projects = {title: Project.from_dict(data) for title, data in load_projects().items()}
        self.tasks = {title: Task.from_dict(data) for title, data in load_tasks().items()}
    
    def save(self):
        save_users({name: user.to_dict() for name, user in self.users.items()})
        save_projects({title: project.to_dict() for title, project in self.projects.items()})
        save_tasks({title: task.to_dict() for title, task in self.tasks.items()})
    
    def add_user(self, name: str, email: str) -> bool:
        if name in self.users:
            return False
        self.users[name] = User(name, email)
        self.save()
        return True
    
    def add_project(self, title: str, description: str, due_date: str, user_name: str) -> bool:
        if title in self.projects or user_name not in self.users:
            return False
        project = Project(title, description, due_date, user_name)
        self.projects[title] = project
        self.users[user_name].projects.append(title)
        self.save()
        return True
    
    def add_task(self, title: str, status: str, assigned_to: str, project_title: str) -> bool:
        if title in self.tasks or project_title not in self.projects:
            return False
        task = Task(title, status, assigned_to, project_title)
        self.tasks[title] = task
        self.projects[project_title].tasks.append(title)
        self.save()
        return True
    
    def update_task_status(self, title: str, new_status: str) -> bool:
        if title not in self.tasks:
            return False
        self.tasks[title].status = new_status
        self.save()
        return True
    
    def list_users(self) -> List[str]:
        return list(self.users.keys())
    
    def list_user_projects(self, user_name: str) -> List[str]:
        if user_name not in self.users:
            return []
        return self.users[user_name].projects
    
    def list_project_tasks(self, project_title: str) -> List[Dict[str, Any]]:
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
