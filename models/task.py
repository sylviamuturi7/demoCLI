#!/usr/bin/env python3

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
