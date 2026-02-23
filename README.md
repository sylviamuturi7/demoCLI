# Project Management CLI Tool

A simple CLI for managing users, projects, and tasks.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py [command] [options]
```

### Commands
- `add-user --name "Alice" --email "alice@example.com"` - Add user
- `add-project --user "Alice" --title "Website" --description "Build website" --due-date "2024-12-01"` - Add project
- `add-task --project "Website" --title "Homepage" --assigned-to "Alice" --status "todo"` - Add task
- `update-task --title "Homepage" --status "done"` - Update task status
- `list-users` - List all users
- `list-projects --user "Alice"` - List user's projects
- `list-tasks --project "Website"` - List project tasks

## File Structure
```
demo_CLI/
├── main.py              # CLI entry point
├── models/              # Class definitions
│   ├── user.py
│   ├── project.py
│   ├── task.py
│   └── manager.py
├── utils/               # Helper functions
│   └── helpers.py
├── data/                # JSON storage
│   ├── users.json
│   ├── projects.json
│   └── tasks.json
└── test_models.py       # Tests
```

## Testing
```bash
python test_models.py
```
