#!/usr/bin/env python3

import unittest
import os
from models.manager import ProjectManager

class TestProjectManager(unittest.TestCase):
    def setUp(self):
        self.pm = ProjectManager()
    
    def test_add_user(self):
        result = self.pm.add_user("Alice", "alice@example.com")
        self.assertTrue(result)
        self.assertIn("Alice", self.pm.users)
        
        result = self.pm.add_user("Alice", "alice2@example.com")
        self.assertFalse(result)
    
    def test_add_project(self):
        self.pm.add_user("Alice", "alice@example.com")
        result = self.pm.add_project("Website", "Build website", "2024-12-01", "Alice")
        self.assertTrue(result)
        self.assertIn("Website", self.pm.projects)
        
        result = self.pm.add_project("Website", "Duplicate", "2024-12-02", "Alice")
        self.assertFalse(result)
    
    def test_add_task(self):
        self.pm.add_user("Alice", "alice@example.com")
        self.pm.add_project("Website", "Build website", "2024-12-01", "Alice")
        result = self.pm.add_task("Homepage", "todo", "Alice", "Website")
        self.assertTrue(result)
        self.assertIn("Homepage", self.pm.tasks)
        
        result = self.pm.add_task("Homepage", "done", "Alice", "Website")
        self.assertFalse(result)
    
    def test_update_task(self):
        self.pm.add_user("Alice", "alice@example.com")
        self.pm.add_project("Website", "Build website", "2024-12-01", "Alice")
        self.pm.add_task("Homepage", "todo", "Alice", "Website")
        
        result = self.pm.update_task_status("Homepage", "done")
        self.assertTrue(result)
        self.assertEqual(self.pm.tasks["Homepage"].status, "done")
        
        result = self.pm.update_task_status("Login", "done")
        self.assertFalse(result)
    
    def test_list_users(self):
        self.pm.add_user("Alice", "alice@example.com")
        self.pm.add_user("Bob", "bob@example.com")
        users = self.pm.list_users()
        self.assertEqual(len(users), 2)
        self.assertIn("Alice", users)
        self.assertIn("Bob", users)
    
    def test_list_projects(self):
        self.pm.add_user("Alice", "alice@example.com")
        self.pm.add_project("Website", "Build website", "2024-12-01", "Alice")
        self.pm.add_project("App", "Mobile app", "2024-12-02", "Alice")
        
        projects = self.pm.list_user_projects("Alice")
        self.assertEqual(len(projects), 2)
        self.assertIn("Website", projects)
        self.assertIn("App", projects)

if __name__ == '__main__':
    unittest.main()
