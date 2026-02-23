#!/usr/bin/env python3

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
