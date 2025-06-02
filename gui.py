import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter task")
add_button = sg.Button("Add")

window = sg.Window("MY To-Do App", layout = [[label], [input_box,add_button]])
window.read()
window.close()