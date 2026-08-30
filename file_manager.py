FILEPATH = "TodoList.txt"


def get_todo_list(filepath=FILEPATH):
    """Read a text file and return the list of todo items"""
    with open(filepath, "r") as file_local:
        todo_list_local = file_local.readlines()
    return todo_list_local


def write_todo_list(todo_list_arg, filepath=FILEPATH):
    """Write the todo list to a text file"""
    with open(filepath, "w") as file_local:
        file_local.writelines(todo_list_arg)