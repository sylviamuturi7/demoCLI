#!/usr/bin/env python3

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
