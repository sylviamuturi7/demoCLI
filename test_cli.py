#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
from main import main

class TestCLI(unittest.TestCase):
    
    def setUp(self):
        # Clean up any existing data files before tests
        data_files = ['data/users.json', 'data/projects.json', 'data/tasks.json']
        for file in data_files:
            if os.path.exists(file):
                os.remove(file)
        # Also remove data directory if empty
        if os.path.exists('data') and not os.listdir('data'):
            os.rmdir('data')
    
    def test_add_user_cli(self):
        with patch('sys.argv', ['main.py', 'add-user', '--name', 'Alice', '--email', 'alice@test.com']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main()
                output = fake_out.getvalue().strip()
                self.assertIn("added successfully", output)
    
    def test_add_duplicate_user_cli(self):
        # Add user first time
        with patch('sys.argv', ['main.py', 'add-user', '--name', 'Alice', '--email', 'alice@test.com']):
            with patch('sys.stdout', new=StringIO()):
                main()
        
        # Try to add same user again - use same ProjectManager instance
        with patch('sys.argv', ['main.py', 'add-user', '--name', 'Alice', '--email', 'alice@test.com']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main()
                output = fake_out.getvalue().strip()
                self.assertIn("already exists", output)
    
    def test_add_project_cli(self):
        # First add a user
        with patch('sys.argv', ['main.py', 'add-user', '--name', 'Alice', '--email', 'alice@test.com']):
            with patch('sys.stdout', new=StringIO()):
                main()
        
        # Then add project - same ProjectManager instance
        with patch('sys.argv', ['main.py', 'add-project', '--user', 'Alice', '--title', 'Website', '--description', 'Build website', '--due-date', '2024-12-01']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main()
                output = fake_out.getvalue().strip()
                self.assertIn("added to user", output)
    
    def test_list_users_cli(self):
        # Add a user first
        with patch('sys.argv', ['main.py', 'add-user', '--name', 'Bob', '--email', 'bob@test.com']):
            with patch('sys.stdout', new=StringIO()):
                main()
        
        # List users - same ProjectManager instance
        with patch('sys.argv', ['main.py', 'list-users']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main()
                output = fake_out.getvalue().strip()
                self.assertIn("Bob", output)
    
    def test_add_task_cli(self):
        # Setup: add user and project first
        with patch('sys.argv', ['main.py', 'add-user', '--name', 'Alice', '--email', 'alice@test.com']):
            with patch('sys.stdout', new=StringIO()):
                main()
        
        with patch('sys.argv', ['main.py', 'add-project', '--user', 'Alice', '--title', 'Website', '--description', 'Build website', '--due-date', '2024-12-01']):
            with patch('sys.stdout', new=StringIO()):
                main()
        
        # Add task - same ProjectManager instance
        with patch('sys.argv', ['main.py', 'add-task', '--project', 'Website', '--title', 'Homepage', '--assigned-to', 'Alice', '--status', 'todo']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                main()
                output = fake_out.getvalue().strip()
                self.assertIn("added", output)

if __name__ == '__main__':
    unittest.main()
