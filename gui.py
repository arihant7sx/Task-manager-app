import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a task")
input_box = sg.InputText(tooltip="Enter task",key = 'task')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_tasks(), key = 'tasks',
                      enable_events=True, size=[35,10])
edit_button = sg.Button("Edit")

window = sg.Window("MY To-Do App",
                   layout = [[label], [input_box,add_button], [list_box, edit_button]],
                   font=("Helvetica",17))
while True:
    event,values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            tasks = functions.get_tasks()
            new_task = values['task'] + '\n'
            tasks.append(new_task)
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)

        case "Edit":
            task_to_edit = values['tasks'][0]
            new_task = values['task']

            tasks = functions.get_tasks()
            index = tasks.index(task_to_edit)
            tasks[index] = new_task
            functions.write_tasks(tasks)
            window['tasks'].update(values=tasks)

        case 'tasks':
            window['task'].update(value=values['tasks'][0])


        case sg.WINDOW_CLOSED:
            break

window.close()