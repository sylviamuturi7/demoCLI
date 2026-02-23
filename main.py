#!/usr/bin/env python3

import argparse
from models.manager import ProjectManager

def main():
    parser = argparse.ArgumentParser(description="Project Management CLI Tool")
    subparsers = parser.add_subparsers(dest='command')
    
    # Add user
    user_parser = subparsers.add_parser('add-user')
    user_parser.add_argument('--name', required=True)
    user_parser.add_argument('--email', required=True)
    
    # Add project
    project_parser = subparsers.add_parser('add-project')
    project_parser.add_argument('--user', required=True)
    project_parser.add_argument('--title', required=True)
    project_parser.add_argument('--description', required=True)
    project_parser.add_argument('--due-date', required=True)
    
    # Add task
    task_parser = subparsers.add_parser('add-task')
    task_parser.add_argument('--project', required=True)
    task_parser.add_argument('--title', required=True)
    task_parser.add_argument('--assigned-to', required=True)
    task_parser.add_argument('--status', default='todo')
    
    # Update task
    update_parser = subparsers.add_parser('update-task')
    update_parser.add_argument('--title', required=True)
    update_parser.add_argument('--status', required=True)
    
    # List commands
    subparsers.add_parser('list-users')
    list_projects_parser = subparsers.add_parser('list-projects')
    list_projects_parser.add_argument('--user', required=True)
    list_tasks_parser = subparsers.add_parser('list-tasks')
    list_tasks_parser.add_argument('--project', required=True)
    
    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return
    
    pm = ProjectManager()
    
    if args.command == 'add-user':
        if pm.add_user(args.name, args.email):
            print(f"User '{args.name}' added successfully!")
        else:
            print(f"User '{args.name}' already exists!")
    
    elif args.command == 'add-project':
        if pm.add_project(args.title, args.description, args.due_date, args.user):
            print(f"Project '{args.title}' added to user '{args.user}'!")
        else:
            print("Failed to add project.")
    
    elif args.command == 'add-task':
        if pm.add_task(args.title, args.status, args.assigned_to, args.project):
            print(f"Task '{args.title}' added!")
        else:
            print("Failed to add task.")
    
    elif args.command == 'update-task':
        if pm.update_task_status(args.title, args.status):
            print(f"Task '{args.title}' updated!")
        else:
            print("Task not found!")
    
    elif args.command == 'list-users':
        users = pm.list_users()
        if users:
            print("Users:")
            for user in users:
                print(f"  - {user} ({pm.users[user].email})")
        else:
            print("No users found.")
    
    elif args.command == 'list-projects':
        projects = pm.list_user_projects(args.user)
        if projects:
            print(f"Projects for '{args.user}':")
            for project in projects:
                print(f"  - {project}")
        else:
            print("No projects found.")
    
    elif args.command == 'list-tasks':
        tasks = pm.list_project_tasks(args.project)
        if tasks:
            print(f"Tasks for '{args.project}':")
            for task in tasks:
                print(f"  [{task['status']}] {task['title']}")
        else:
            print("No tasks found.")

if __name__ == "__main__":
    main()
