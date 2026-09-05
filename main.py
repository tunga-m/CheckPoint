import time

import actions


def menu():
    current_time = time.strftime("%b %d, %Y %H:%M:%S")
    print("Current date and time: " + current_time)

    while True:
        user_input = input("Enter 'add', 'show', 'edit', 'complete', or 'exit': ")
        user_input = user_input.lower().strip()

        if user_input.startswith('add '):
            actions.add_todo(user_input)
        elif user_input.startswith('edit '):
            try:
                actions.edit_todo(user_input)
            except ValueError:
                print("Invalid input, enter the index of the item you want to edit...")
            except IndexError:
                print("Invalid input, index is out of range...")
        elif user_input.startswith('complete '):
            try:
                actions.complete_todo(user_input)
            except IndexError:
                print("Invalid input, index is out of range...")
            except ValueError:
                print("Invalid input, enter the index of the item you want to complete...")
        elif user_input == 'show':
            actions.show_todo_list()
        elif user_input == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid input...")


if __name__ == "__main__":
    menu()