#!/usr/bin/env python3

import unittest
import os
import sys
from models import ProjectManager

class TestCLIIntegration(unittest.TestCase):
    
    def setUp(self):
        # Clean up any existing data files before tests
        data_files = ['data/users.json', 'data/projects.json', 'data/tasks.json']
        for file in data_files:
            if os.path.exists(file):
                os.remove(file)
        # Also remove data directory if empty
        if os.path.exists('data') and not os.listdir('data'):
            os.rmdir('data')
        
        # Create fresh ProjectManager for each test
        self.pm = ProjectManager()
    
    def test_full_workflow(self):
        # Test adding user
        result = self.pm.add_user("Alice", "alice@test.com")
        self.assertTrue(result)
        self.assertIn("Alice", self.pm.users)
        
        # Test adding project
        result = self.pm.add_project("Website", "Build website", "2024-12-01", "Alice")
        self.assertTrue(result)
        self.assertIn("Website", self.pm.projects)
        
        # Test adding task
        result = self.pm.add_task("Homepage", "todo", "Alice", "Website")
        self.assertTrue(result)
        self.assertIn("Homepage", self.pm.tasks)
        
        # Test listing users
        users = self.pm.list_users()
        self.assertIn("Alice", users)
        
        # Test listing projects
        projects = self.pm.list_user_projects("Alice")
        self.assertIn("Website", projects)
        
        # Test listing tasks
        tasks = self.pm.list_project_tasks("Website")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Homepage")
        
        # Test updating task
        result = self.pm.update_task_status("Homepage", "done")
        self.assertTrue(result)
        self.assertEqual(self.pm.tasks["Homepage"].status, "done")
    
    def test_duplicate_user(self):
        # Add user first time
        result = self.pm.add_user("Bob", "bob@test.com")
        self.assertTrue(result)
        
        # Try to add same user again
        result = self.pm.add_user("Bob", "bob2@test.com")
        self.assertFalse(result)
    
    def test_project_without_user(self):
        # Try to add project without user
        result = self.pm.add_project("App", "Mobile app", "2024-12-02", "NonExistent")
        self.assertFalse(result)
    
    def test_task_without_project(self):
        # Try to add task without project
        result = self.pm.add_task("Login", "todo", "Alice", "NonExistent")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
