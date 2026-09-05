import FreeSimpleGUI as sg

import actions

label = sg.Text("Enter a task:")
input_box = sg.InputText(tooltip="Type your task here")
add_button = sg.Button("Add", tooltip="Click to add the task")

window = sg.Window("CheckPoint", layout=[[label], [input_box, add_button]]) 
window.read()
window.close()