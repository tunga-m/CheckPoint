import FreeSimpleGUI as sg

import actions  # noqa: F401
import file_manager

label = sg.Text("Enter a task:")
input_box = sg.InputText(tooltip="Type your task here")
add_button = sg.Button("Add", tooltip="Click to add the task", key="add_task")

window = sg.Window(
                   "CheckPoint", 
                   layout=[[label], [input_box, add_button]], 
                   font=("Helvetica", 15)
                  )

while True: 
    event, values = window.read()
    match event:
        case "Add":
            todo_list = file_manager.get_todo_list()
            new_task = values['add_task'] + "\n"
            todo_list.append(new_task)
            file_manager.write_todo_list(todo_list)
        case sg.WINDOW_CLOSED:
            break

window.close()