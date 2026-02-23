#!/usr/bin/env python3

import json
import os

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
PROJECTS_FILE = os.path.join(DATA_DIR, "projects.json")
TASKS_FILE = os.path.join(DATA_DIR, "tasks.json")

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_users():
    ensure_data_dir()
    if not os.path.exists(USERS_FILE):
        return {}
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_users(users):
    ensure_data_dir()
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def load_projects():
    ensure_data_dir()
    if not os.path.exists(PROJECTS_FILE):
        return {}
    try:
        with open(PROJECTS_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_projects(projects):
    ensure_data_dir()
    with open(PROJECTS_FILE, 'w') as f:
        json.dump(projects, f, indent=2)

def load_tasks():
    ensure_data_dir()
    if not os.path.exists(TASKS_FILE):
        return {}
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except:
        return {}

def save_tasks(tasks):
    ensure_data_dir()
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)
