# Project Management CLI Tool

This is a command-line tool I built to help manage users, projects, and tasks. It's pretty straightforward to use and stores everything locally in JSON files.

## Getting Started

First, you'll need to install the dependencies. Just run:
```bash
pip install -r requirements.txt
```

## How to Use It

The basic format is:

```bash
python main.py [command] [options]
```

### Available Commands

Here's what you can do with this tool:

**Managing Users:**
- `add-user --name "Alice" --email "alice@example.com"` - Creates a new user
- `list-users` - Shows all users in the system

**Managing Projects:**
- `add-project --user "Alice" --title "Website" --description "Build website" --due-date "2024-12-01"` - Adds a project to a user
- `list-projects --user "Alice"` - Shows all projects for a specific user

**Managing Tasks:**
- `add-task --project "Website" --title "Homepage" --assigned-to "Alice" --status "todo"` - Creates a task for a project
- `update-task --title "Homepage" --status "done"` - Updates the status of a task
- `list-tasks --project "Website"` - Lists all tasks in a project

## Project Structure

I organized the code into different folders to keep things clean:

```
demo_CLI/
├── main.py              # This is where the CLI starts
├── models/              # All the class definitions
│   ├── user.py
│   ├── project.py
│   ├── task.py
│   └── manager.py
├── utils/               # Some helper functions I wrote
│   └── helpers.py
├── data/                # Where all the data gets saved
│   ├── users.json
│   ├── projects.json
│   └── tasks.json
└── test_models.py       # Unit tests
```

## Running Tests

I included some tests to make sure everything works correctly. You can run them with:

```bash
python test_models.py
```

## Common Issues

- The tool expects exact matches for user and project names when adding tasks or projects
- Date validation could be more robust

Feel free to reach out if you run into any problems!
