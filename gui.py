import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter task",key = 'task')
add_button = sg.Button("Add")

window = sg.Window("MY To-Do App",
                   layout = [[label], [input_box,add_button]],
                   font=("Helvetica",17))
while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "add":
            tasks = functions.get_tasks()
            new_task = values['task'] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)

        case sg.WINDOW_CLOSED:
            break

window.close()