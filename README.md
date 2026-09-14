# CheckPoint

CheckPoint is a Python task-management application currently being refactored from a simple text-file based program into a structured, database-backed desktop application.

The project originally began as a command-line todo application and later gained a graphical interface using FreeSimpleGUI. The current development branch focuses on replacing flat-file persistence with SQLite and introducing a cleaner application architecture that can later support an API, containerization, automated testing, and deployment workflows.

## Current Development Status

**Branch:** `feature/sqlite-persistence`

The current development milestone is migrating CheckPoint from:

```text
FreeSimpleGUI
     ↓
file_manager.py
     ↓
TodoList.txt
```

to:

```text
FreeSimpleGUI
     ↓
SQLite persistence layer
     ↓
checkpoint.db
```

The SQLite persistence layer is implemented and tested independently. The next stage is integrating it into the graphical interface.

## Current Project Structure

```text
CheckPoint/
│
├── CheckPoint.py
├── database.py
├── cli.py
├── actions.py
├── file_manager.py
├── requirements.txt
├── README.md
├── .gitignore
└── CheckPoint.spec
```

### `CheckPoint.py`

The current graphical interface built with FreeSimpleGUI.

The GUI currently uses the legacy text-file persistence system and will be migrated to SQLite in the next development phase.

### `database.py`

The new SQLite persistence layer.

It currently supports:

* Database initialization
* Task creation
* Task retrieval
* Retrieval by task ID
* Filtering tasks by status
* Task editing
* Task completion
* Reopening completed tasks
* Permanent task deletion
* Parameterized SQL queries
* Transaction handling
* Automatic connection cleanup
* Database constraints and default values

### `cli.py`

Legacy command-line interface from the original version of CheckPoint.

The CLI currently relies on the older text-file implementation and is not planned as part of the primary modernized application.

### `actions.py`

Contains logic used by the original command-line version.

This module is considered part of the legacy implementation and may be retired once the SQLite-backed application is complete.

### `file_manager.py`

Handles the original `TodoList.txt` persistence system.

This module will eventually be removed once SQLite fully replaces text-file storage.

## SQLite Task Model

Tasks are now stored as structured database records rather than individual lines of text.

The current `tasks` table contains:

| Column         | Purpose                                        |
| -------------- | ---------------------------------------------- |
| `id`           | Unique task identifier                         |
| `title`        | Required task title                            |
| `description`  | Optional task details                          |
| `status`       | `active` or `completed`                        |
| `priority`     | `low`, `medium`, or `high`                     |
| `created_at`   | Timestamp generated when the task is created   |
| `due_at`       | Optional due date/time                         |
| `completed_at` | Timestamp generated when the task is completed |

Example:

```text
id:           1
title:        Finish CheckPoint database layer
description:  Complete SQLite persistence implementation
status:       active
priority:     high
created_at:   2026-09-13 20:00:00
due_at:       NULL
completed_at: NULL
```

## Database Design

CheckPoint uses SQLite through Python's built-in `sqlite3` module.

The persistence layer currently includes several reliability and data-integrity features.

### Primary Keys

Every task receives a unique numeric ID.

This allows tasks to be identified independently of their title or list position.

Two tasks may therefore share the same title while remaining separate records.

### Constraints

The database enforces several rules directly in the schema.

Task titles cannot be `NULL` or contain only whitespace.

Valid task statuses are limited to:

```text
active
completed
```

Valid priorities are limited to:

```text
low
medium
high
```

### Parameterized Queries

User and application values are passed to SQLite using query parameters rather than being inserted directly into SQL strings.

Example:

```python
WHERE id = ?
```

This keeps SQL structure separate from application data and avoids unsafe SQL construction.

### Transaction Handling

Database connections are managed through a reusable context manager.

Write operations automatically:

```text
open connection
      ↓
execute database operation
      ↓
success → commit
failure → rollback
      ↓
close connection
```

This reduces duplicated connection-management code and helps prevent partially applied database operations.

### Task Completion

Completing a task does not delete the database record.

Instead:

```text
status = completed
completed_at = timestamp
```

This preserves task history and allows completed tasks to later be viewed or reopened.

Permanent deletion exists as a separate operation.

## Current Features

The existing application currently supports:

* [x] Desktop GUI
* [x] Add tasks
* [x] Edit tasks
* [x] Complete tasks
* [x] Local task persistence
* [x] Windows executable packaging with PyInstaller
* [x] SQLite database schema
* [x] Unique task IDs
* [x] Structured task records
* [x] Task priorities
* [x] Optional descriptions
* [x] Optional due dates
* [x] Active and completed task states
* [x] Completion timestamps
* [x] Reopen completed tasks at the database layer
* [x] Permanent deletion at the database layer
* [x] Transaction-safe database access
* [x] Parameterized SQL
* [ ] SQLite-backed GUI
* [ ] Completed-task GUI view
* [ ] Priority controls in GUI
* [ ] Description controls in GUI
* [ ] Due-date controls in GUI
* [ ] Retire `TodoList.txt`
* [ ] Retire legacy file-based persistence

## Development Roadmap

### Phase 1 — Original Application

```text
Python
FreeSimpleGUI / CLI
TodoList.txt
```

Completed.

### Phase 2 — SQLite Persistence

```text
FreeSimpleGUI
     ↓
Application Logic
     ↓
SQLite
```

**Current phase.**

Completed:

* Database schema
* CRUD operations
* Task status tracking
* Connection management
* Transaction handling
* Data constraints

Next:

* Integrate SQLite with the GUI
* Display active tasks using database records
* Track task IDs in GUI selections
* Support descriptions, priorities, and due dates
* Add completed-task history
* Retire legacy text-file persistence

### Phase 3 — Application Architecture

Planned improvements include separating interface logic from business logic.

Target architecture:

```text
Desktop GUI
     ↓
Task Service
     ↓
Persistence Layer
```

This will allow future clients to reuse the same application behavior without duplicating task logic.

### Phase 4 — REST API

Planned:

* FastAPI backend
* REST endpoints
* Structured request and response models
* API validation
* API documentation
* Client/server architecture

Target architecture:

```text
Client
  ↓
FastAPI
  ↓
Service Layer
  ↓
Database
```

### Phase 5 — PostgreSQL and Containers

Planned:

* PostgreSQL
* Docker
* Docker Compose
* Persistent database volumes
* Container networking
* Environment-based configuration
* Health checks

### Phase 6 — Testing and CI/CD

Planned:

* Pytest
* Unit testing
* Integration testing
* API testing
* GitHub Actions
* Automated build and test workflows

### Phase 7 — DevSecOps

Planned:

* Static application security scanning
* Dependency vulnerability scanning
* Container image scanning
* Secure secrets management
* Secure runtime configuration

### Phase 8 — Linux Deployment

Planned:

* Linux deployment
* Logging
* Service health monitoring
* Persistent storage
* Restart behavior
* Deployment documentation

## Technologies

### Currently Used

* Python
* SQLite
* SQL
* FreeSimpleGUI
* Git
* GitHub
* PyInstaller

### Planned

* FastAPI
* PostgreSQL
* Docker
* Docker Compose
* Pytest
* GitHub Actions
* Linux deployment tooling
* Application and container security scanning

## Development Concepts Practiced

CheckPoint is being used as a hands-on project for learning and applying:

* Python application development
* Event-driven programming
* Relational database design
* SQL
* Primary keys
* Database constraints
* CRUD operations
* Transactions
* Context managers
* Parameterized queries
* Persistent storage
* Application state
* Separation of concerns
* Git branching workflows
* Incremental refactoring
* Application packaging

## Branching Strategy

Stable application code remains on:

```text
main
```

Major development work is performed on feature branches.

The current database refactor is being developed on:

```text
feature/sqlite-persistence
```

The feature branch will be merged into `main` once SQLite is fully integrated into the graphical application and the legacy persistence path is no longer required.

## Running the Current Application

Create and activate a Python virtual environment, then install dependencies:

```bash
pip install -r requirements.txt
```

Run the graphical application:

```bash
python CheckPoint.py
```

The SQLite persistence module is currently being integrated and may not yet be the storage backend used by the graphical interface on this branch.

## Project Goal

CheckPoint began as a small Python todo application, but the long-term purpose of the project is to practice evolving a simple application into a more production-style system.

The project is intended to demonstrate the progression from:

```text
local script
     ↓
desktop application
     ↓
relational database
     ↓
layered architecture
     ↓
REST API
     ↓
containerized services
     ↓
automated testing and CI/CD
     ↓
security automation
     ↓
Linux deployment
```

The focus is not only on implementing features, but also on understanding the architectural and operational decisions behind each stage.
