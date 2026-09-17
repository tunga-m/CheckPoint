import database

VALID_PRIORITIES = ("low", "medium", "high")

class TaskNotFoundError(Exception):
    """Raised when a requested task does not exist."""


def create_task(title, description=None, priority="medium", due_at=None):
    """Validate and create a new task in the database."""
    title = title.strip()

    if not title:
        raise ValueError("Task title cannot be empty.")

    priority = priority.strip().lower()

    if priority not in VALID_PRIORITIES:
        raise ValueError(f"Priority must be one of {VALID_PRIORITIES}.")

    if description is not None:
        description = description.strip()

        if not description:
            description = None

    return database.add_task(title=title, 
                             description=description, 
                             priority=priority, 
                             due_at=due_at)


def get_task(task_id):
    """Retrieve a task or raise an error if it does not exist."""
    task = database.get_task_by_id(task_id)

    if task is None:
        raise TaskNotFoundError(
            f"Task with ID {task_id} was not found."
        )

    return task