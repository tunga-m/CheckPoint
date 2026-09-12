import FreeSimpleGUI as sg

import file_manager

APP_TITLE = "CheckPoint"
WINDOW_FONT = ("Helvetica", 15)
LIST_SIZE = (44, 10)

sg.theme("SystemDefaultForReal")


def load_tasks():
    """Load the current todo list from storage."""
    return file_manager.get_todo_list()


def refresh_task_list(window):
    """Refresh the Listbox using the latest data from storage."""
    window["todo_list"].update(values=load_tasks())


def clear_input(window):
    """Clear the task input field and return focus to it."""
    window["task_input"].update("")
    window["task_input"].set_focus()


def task_exists(task_name, todo_list, excluded_index=None):
    """
    Check whether a task already exists.

    excluded_index is used when editing so the currently selected
    task is not considered a duplicate of itself.
    """
    normalized_task = task_name.strip().casefold()

    for index, task in enumerate(todo_list):
        if index == excluded_index:
            continue

        if task.strip().casefold() == normalized_task:
            return True

    return False


def add_task(window, values):
    """Add a new task to the todo list."""
    new_task = values["task_input"].strip()

    if not new_task:
        sg.popup_error(
            "Please enter a task before clicking Add.",
            title="Invalid Task"
        )
        return

    todo_list = load_tasks()

    if task_exists(new_task, todo_list):
        sg.popup_error(
            f'The task "{new_task}" already exists.',
            title="Duplicate Task"
        )
        return

    todo_list.append(new_task + "\n")
    file_manager.write_todo_list(todo_list)

    clear_input(window)
    refresh_task_list(window)


def edit_task(window, values):
    """Edit the currently selected task."""
    selected_indexes = window["todo_list"].get_indexes()

    if not selected_indexes:
        sg.popup_error(
            "Please select a task to edit.",
            title="No Task Selected"
        )
        return

    new_task = values["task_input"].strip()

    if not new_task:
        sg.popup_error(
            "The task cannot be empty.",
            title="Invalid Task"
        )
        return

    selected_index = selected_indexes[0]
    todo_list = load_tasks()

    if task_exists(
        new_task,
        todo_list,
        excluded_index=selected_index
    ):
        sg.popup_error(
            f'The task "{new_task}" already exists.',
            title="Duplicate Task"
        )
        return

    todo_list[selected_index] = new_task + "\n"
    file_manager.write_todo_list(todo_list)

    clear_input(window)
    refresh_task_list(window)


def complete_task(window):
    """Remove the currently selected task from the todo list."""
    selected_indexes = window["todo_list"].get_indexes()

    if not selected_indexes:
        sg.popup_error(
            "Please select a task to complete.",
            title="No Task Selected"
        )
        return

    selected_index = selected_indexes[0]
    todo_list = load_tasks()

    completed_task = todo_list[selected_index].strip()

    todo_list.pop(selected_index)
    file_manager.write_todo_list(todo_list)

    clear_input(window)
    refresh_task_list(window)

    sg.popup(
        f'Task "{completed_task}" has been completed.',
        title="Task Completed"
    )


def populate_input_from_selection(window, values):
    """Place the selected task into the input field for editing."""
    selected_tasks = values["todo_list"]

    if not selected_tasks:
        return

    selected_task = selected_tasks[0].strip()

    window["task_input"].update(selected_task)
    window["task_input"].set_focus()


def create_window():
    """Create and return the application's main window."""
    label = sg.Text("Enter a task:")

    input_box = sg.InputText(
        tooltip="Type your task here",
        key="task_input",
        size=(45, 1)
    )

    add_button = sg.Button(
        "Add",
        tooltip="Add a new task",
        key="add_task"
    )

    edit_button = sg.Button(
        "Edit",
        tooltip="Edit the selected task",
        key="edit_task"
    )

    complete_button = sg.Button(
        "Complete",
        tooltip="Mark the selected task as complete",
        key="complete_task"
    )

    list_box = sg.Listbox(
        values=load_tasks(),
        key="todo_list",
        enable_events=True,
        size=LIST_SIZE,
        select_mode=sg.LISTBOX_SELECT_MODE_SINGLE
    )

    layout = [
        [list_box],
        [label],
        [input_box],
        [add_button, edit_button, complete_button]
    ]

    return sg.Window(
        APP_TITLE,
        layout=layout,
        font=WINDOW_FONT
    )


def main():
    """Run the CheckPoint application."""
    window = create_window()

    try:
        while True:
            event, values = window.read()

            match event:
                case sg.WINDOW_CLOSED:
                    break

                case "add_task":
                    add_task(window, values)

                case "edit_task":
                    edit_task(window, values)

                case "complete_task":
                    complete_task(window)

                case "todo_list":
                    populate_input_from_selection(window, values)

    finally:
        window.close()


if __name__ == "__main__":
    main()