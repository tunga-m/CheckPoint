import FreeSimpleGUI as sg

import file_manager

label = sg.Text("Enter a task:")

input_box = sg.InputText(tooltip="Type your task here",
                         key="task_input")

add_button = sg.Button("Add", 
                       tooltip="Click to add the task", 
                       key="add_task")

edit_button = sg.Button("Edit")

complete_button = sg.Button("Complete")

list_box = sg.Listbox(values=file_manager.get_todo_list(),
                      key="todo_list", 
                      enable_events=True, 
                      size=(45, 10))

layout = [[list_box], 
          [label], 
          [input_box], 
          [add_button, edit_button, complete_button]]

window = sg.Window(
                   "CheckPoint", 
                   layout=layout, 
                   font=("Helvetica", 15)
                  )

while True: 
    event, values = window.read()

    match event:
        case "add_task":
            new_task = values['task_input'].strip()

            if new_task:
                todo_list = file_manager.get_todo_list()
                todo_list.append(new_task + "\n")
                file_manager.write_todo_list(todo_list)

                window["task_input"].update("")  # Clear the input box after adding the task
                window["todo_list"].update(values=file_manager.get_todo_list())
        case "Edit":
            if values['todo_list']:
                task_to_edit = values['todo_list'][0]
                new_task = values['task_input'].strip()

                if new_task:
                    todo_list = file_manager.get_todo_list()
                    index = todo_list.index(task_to_edit)
                    todo_list[index] = new_task + "\n"
                    file_manager.write_todo_list(todo_list)

                    window["task_input"].update("")  # Clear the input box after editing the task
                    window["todo_list"].update(values=file_manager.get_todo_list())  # Refresh the listbox
        case "todo_list":
            if values['todo_list']:
                window["task_input"].update(
                    value=values['todo_list'][0].strip())  # Populate the input box with the selected task
        case "Complete":
            if values['todo_list']:
                task_to_complete = values['todo_list'][0]
                todo_list = file_manager.get_todo_list()
                todo_list.remove(task_to_complete)
                file_manager.write_todo_list(todo_list)

                window["task_input"].update("")  # Clear the input box after completing the task
                window["todo_list"].update(values=file_manager.get_todo_list())  # Refresh the listbox
        case sg.WINDOW_CLOSED:
            break

window.close()