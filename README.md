# CheckPoint

CheckPoint is a lightweight desktop task manager built with Python and FreeSimpleGUI. It provides a simple graphical interface for creating, editing, completing, and managing everyday tasks while saving them locally between sessions.

The project began as a command-line Python todo application and was later expanded into a desktop GUI application as part of my continued Python development practice.

## Features

* Add new tasks
* Edit existing tasks
* Mark tasks as complete
* Select tasks directly from the task list
* Prevent duplicate tasks
* Validate empty or invalid input
* Save tasks between application sessions
* Automatically refresh the interface after changes
* Windows executable built with PyInstaller
* User-friendly popup messages for errors and completed tasks

## Technologies Used

* Python
* FreeSimpleGUI
* PyInstaller
* Git
* GitHub

## Application Architecture

CheckPoint separates the graphical interface from file-management functionality.

```text
CheckPoint/
│
├── gui.py
├── file_manager.py
├── actions.py
├── CheckPoint.spec
├── requirements.txt
├── README.md
└── .gitignore
```

### `gui.py`

Handles the graphical user interface and event-driven application logic, including:

* Adding tasks
* Editing tasks
* Completing tasks
* Selecting tasks
* Input validation
* Updating GUI elements

### `file_manager.py`

Handles persistent task storage, including reading and writing the todo list.

### `actions.py`

Contains task-related functionality developed during the earlier command-line version of CheckPoint.

## How It Works

When the application starts, CheckPoint loads the existing task list from local storage.

The GUI then waits for user-generated events such as:

```text
Add
Edit
Complete
Task Selection
Window Close
```

Each event is routed to the appropriate application logic.

For example:

```text
User enters task
        ↓
Clicks Add
        ↓
Input is validated
        ↓
Task is saved
        ↓
Task list is refreshed
```

Tasks are currently stored locally in `TodoList.txt`.

The runtime task file is excluded from Git so each user maintains their own local task data.

## Duplicate Task Handling

CheckPoint prevents duplicate task names from being added.

Before saving a task, existing tasks are normalized and compared against the new task. This helps prevent accidental duplicate entries and keeps the task list organized.

Editing also excludes the currently selected task from duplicate checking so a task is not incorrectly detected as a duplicate of itself.

## Input Validation

The application validates user actions before modifying stored data.

Examples include:

* Preventing empty tasks
* Preventing duplicate tasks
* Preventing editing without a selected task
* Preventing completing a task without a selected task

The application provides popup feedback when an invalid action occurs.

## Running From Source

### 1. Clone the repository

```bash
git clone https://github.com/tunga-m/CheckPoint.git
cd CheckPoint
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run CheckPoint

```bash
python gui.py
```

## Building the Windows Executable

CheckPoint can be packaged as a standalone Windows executable using PyInstaller.

Using the included PyInstaller specification file:

```bash
pyinstaller CheckPoint.spec
```

The generated executable will be placed in the:

```text
dist/
```

directory.

PyInstaller-generated `build/` and `dist/` directories are excluded from source control.

## Windows Release

Compiled Windows releases can be distributed through the GitHub **Releases** section rather than storing executable files directly in the source repository.

This keeps the repository focused on source code while still allowing users to download a packaged version of CheckPoint.

## Development Concepts Practiced

This project provided hands-on experience with several Python and software-development concepts:

* Event-driven programming
* GUI development
* Functions and modular design
* File I/O
* Persistent application data
* Lists and indexing
* String normalization
* Input validation
* Exception prevention
* Separation of concerns
* Virtual environments
* Dependency management
* Git version control
* Application packaging with PyInstaller

## Reliability and Validation

CheckPoint includes defensive checks around user-generated input and GUI state.

Rather than assuming that a valid task or selection always exists, the application checks application state before performing operations.

For example, Edit and Complete operations identify the selected list position instead of searching for a task solely by its text value. This prevents incorrect behavior when task values would otherwise be ambiguous.

## Future Improvements

Potential future versions of CheckPoint may include:

* Unique task IDs
* SQLite database storage
* Completed-task history
* Due dates
* Task priorities
* Task categories
* Search and filtering
* Sort options
* Keyboard shortcuts
* Improved visual styling
* Dark mode
* Creation and completion timestamps
* Automated testing
* Application installer
* Cross-platform packaging

A future database-backed version could store tasks as structured records instead of individual lines in a text file.

For example:

```text
Task
├── ID
├── Title
├── Status
├── Created At
└── Completed At
```

This would allow CheckPoint to scale beyond its current lightweight file-based architecture.

## Project Status

**Current Version:** `v1.0`

Core functionality is implemented:

* [x] Add tasks
* [x] Display tasks
* [x] Edit tasks
* [x] Complete tasks
* [x] Persistent storage
* [x] Duplicate validation
* [x] User input validation
* [x] Desktop GUI
* [x] Windows executable
* [ ] SQLite persistence
* [ ] Completed-task history
* [ ] Automated tests
* [ ] Advanced task organization

## Author

**Tunga Markal**

B.S. Information Technology — Software Engineering
