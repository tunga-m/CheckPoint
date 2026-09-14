from multiprocessing.dummy import connection
import sqlite3
from contextlib import contextmanager
from pathlib import Path

DATABASE_PATH = Path(__file__).resolve().parent / "checkpoint.db"


def get_connection():
    """Establish a connection to the SQLite database."""
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row  # Enable named column access
    return connection


@contextmanager
def database_connection():
    """Provide a database connection with automatic transaction handling."""
    connection = get_connection()

    try:
        yield connection
        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()


def initialize_database():
    """Create the tasks table if it doesn't exist."""
    connection = get_connection()

    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT NOT NULL
                CHECK(length(trim(title)) > 0),

            description TEXT,

            status TEXT NOT NULL DEFAULT 'active'
                CHECK(status IN ('active', 'completed')),

            priority TEXT NOT NULL DEFAULT 'medium'
                CHECK(priority IN ('low', 'medium', 'high')),

            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,

            due_at TEXT,

            completed_at TEXT
        )
        """
    )

    connection.close()


def add_task(title, description=None, priority="medium", due_at=None):
    """Add a new task to the database."""
    with database_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO tasks (
                title,
                description,
                priority,
                due_at
            )
            VALUES (?, ?, ?, ?)
            """,
            (title, description, priority, due_at)
        )

        return cursor.lastrowid


def get_tasks():
    """Retrieve all tasks from the database."""
    connection = get_connection()

    rows = connection.execute(
        """
        SELECT
            id,
            title,
            description,
            status,
            priority,
            created_at,
            due_at,
            completed_at
        FROM tasks
        """
    ).fetchall()

    connection.close()

    return rows


def update_task(task_id, title, description=None, priority="medium", due_at=None):
    """Update the editable fields of a task by its ID."""
    with database_connection() as connection:
        connection.execute(
            """
            UPDATE tasks
            SET 
                title = ?,
                description = ?,
                priority = ?,
                due_at = ?
            WHERE id = ?
            """,
            (title, description, priority, due_at, task_id)
        )


def complete_task(task_id):
    """Mark a task as completed without deleting it."""
    with database_connection() as connection:
        connection.execute(
            """
            UPDATE tasks
            SET
            status = 'completed',
            completed_at = CURRENT_TIMESTAMP
        WHERE id = ?
        """,
        (task_id,)
    )


def get_tasks_by_status(status):
    """Retrieve tasks matching a specific status."""
    connection = get_connection()

    rows = connection.execute(
        """
        SELECT
            id,
            title,
            description,
            status,
            priority,
            created_at,
            due_at,
            completed_at
        FROM tasks
        WHERE status = ?
        """,
        (status,)
    ).fetchall()

    connection.close()

    return rows


def get_active_tasks():
    """Retrieve only active tasks from the database."""
    return get_tasks_by_status('active')


def get_completed_tasks():
    """Retrieve only completed tasks from the database."""
    return get_tasks_by_status('completed')


def get_task_by_id(task_id):
    """Retrieve a single task by its unique ID."""
    connection = get_connection()

    row = connection.execute(
        """
        SELECT
            id,
            title,
            description,
            status,
            priority,
            created_at,
            due_at,
            completed_at
        FROM tasks
        WHERE id = ?
        """,
        (task_id,)
    ).fetchone()

    connection.close()

    return row


def reopen_task(task_id):
    """Reopen a completed task and clear its completion timestamp."""
    with database_connection() as connection:
        connection.execute(
            """
            UPDATE tasks
            SET
                status = 'active',
                completed_at = NULL
            WHERE id = ?
            """,
            (task_id,)
        )


def delete_task(task_id):
    """Permanently delete a task by its ID."""
    with database_connection() as connection:
        connection.execute(
            """
            DELETE FROM tasks
            WHERE id = ?
            """,
            (task_id,)
        )