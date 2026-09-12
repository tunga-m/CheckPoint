import FreeSimpleGUI as sg

import actions  # noqa: F401
import file_manager

label = sg.Text("Enter a task:")
input_box = sg.InputText(tooltip="Type your task here", key="task_input")
add_button = sg.Button("Add", tooltip="Click to add the task", key="add_task")

window = sg.Window(
                   "CheckPoint", 
                   layout=[[label], [input_box, add_button]], 
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
        case sg.WINDOW_CLOSED:
            break

window.close()