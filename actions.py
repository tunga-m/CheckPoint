import file_manager


def add_todo(user_input):
    """Add a new todo item to the todo_list"""
    todo = user_input[4:].strip()

    if not todo:
        raise ValueError("Todo item cannot be empty.")

    todo_list = file_manager.get_todo_list()
    todo_list.append(todo + "\n")

    file_manager.write_todo_list(todo_list)


def edit_todo(user_input):
    """Edit an existing todo item in the todo_list"""
    item_index = get_todo_index(user_input)

    negative_index_check(item_index)

    todo_list = file_manager.get_todo_list()

    print(todo_list[item_index])
    new_todo = input("Enter a new todo: ")
    todo_list[item_index] = new_todo + '\n'

    file_manager.write_todo_list(todo_list)


def complete_todo(user_input):
    """Complete a todo item and remove it from the list"""
    todo_completed = get_todo_index(user_input)

    negative_index_check(todo_completed)

    todo_list = file_manager.get_todo_list()

    print(f"{todo_list[todo_completed].strip('\n')} has been completed.\n")
    todo_list.pop(todo_completed)

    file_manager.write_todo_list(todo_list)
    print("Completed successfully!\n")
    show_todo_list()


def show_todo_list():
    """Display the current todo list"""
    todo_list = file_manager.get_todo_list()

    for index, todo in enumerate(todo_list):
        print(f"{index + 1} - {todo.strip('\n')}.")


def get_todo_index(user_input):
    """Get the index of a todo item from the user input"""
    index = int(user_input.split()[1])
    return index - 1  # Convert to zero-based index


def negative_index_check(index):
    """Check if the index is negative and raise an IndexError if it is"""
    if index < 1:
        raise IndexError("Index cannot be negative.")