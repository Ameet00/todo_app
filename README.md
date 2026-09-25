# Todo App

A simple command-line Todo application built with Python.

The application allows users to add, view, complete, and delete tasks. Tasks are stored locally in a JSON file, so they remain available after the application is closed.

## Features

- Add a new task
- List all tasks
- Mark a task as completed
- Delete a task
- Store tasks in a JSON file
- Command-line interface using `argparse`

## Technologies

- Python 3
- JSON
- `argparse`
- `os`

## Project Structure

```text
todo_app/
│
├── main.py
├── tasks.json
├── README.md
└── .gitignore
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Ameet00/todo_app.git
```

### 2. Navigate to the project folder

```bash
cd todo_app
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

### 5. Run the application

```bash
python main.py
```

## Usage

The application is controlled through commands.

### Add a task

```bash
python main.py Add "Learn Python"
```

### List tasks

```bash
python main.py List
```

Example output:

```text
1.[].Learn Python
2.[x].Complete homework
```

### Complete a task

```bash
python main.py Done 1
```

This marks task `1` as completed.

### Delete a task

```bash
python main.py Delete 1
```

This deletes task `1`.

### Show available commands

```bash
python main.py --help
```

## Data Storage

Tasks are stored in a local `tasks.json` file.

Each task contains:

```json
{
  "id": 1,
  "title": "Learn Python",
  "done": false
}
```

Where:

- `id` — unique task identifier
- `title` — task description
- `done` — whether the task has been completed

## Example Workflow

```bash
python main.py Add "Study Python"
python main.py Add "Finish university project"
python main.py List
python main.py Done 1
python main.py List
python main.py Delete 2
python main.py List
```

## Future Improvements

Possible improvements for the project:

- Edit an existing task
- Add task priorities
- Add due dates
- Search for tasks
- Filter completed/uncompleted tasks
- Improve task ID management after deletion
- Add automated tests
- Add a graphical user interface

## Author

**Ameet00**

GitHub: https://github.com/Ameet00