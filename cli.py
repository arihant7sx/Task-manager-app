import functions
import time

now = time.strftime("%d-%y-%m %H:%M:%S")
print("It is: ",now)
while True:
    user_choice = input("Type add, show, edit, complete or exit: ")
    user_choice  = user_choice.strip()

    if user_choice.startswith("add"):
        task = user_choice[4:]

        tasks = functions.get_tasks()

        tasks.append(task + '\n')

        functions.write_tasks(tasks,)

    elif user_choice.startswith("show"):

        tasks = functions.get_tasks()
        for index,item in enumerate(tasks):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_choice.startswith("edit"):
        try:
            number = int(user_choice[5:])
            print(number)

            number = number - 1

            tasks = functions.get_tasks()

            new_task = input("Enter the new task: ")
            tasks[number] = new_task + '\n'

            functions.write_tasks(tasks,)
        except ValueError:
            print("Invalid command")
            continue


    elif user_choice.startswith("complete"):
        try:
            number=int(user_choice[9:])
            tasks = functions.get_tasks()
            index = number-1
            task_to_remove=tasks[index].strip('\n')
            tasks.pop(index)
            functions.write_tasks(tasks,)

            message=f"Task {task_to_remove} has been removed from the list"
            print(message)
        except IndexError:
            print("No task with such number")
            continue
        except ValueError:
            print("Add the number of task to be removed")
            continue

    elif user_choice.startswith("exit"):
        break

    else:
        print("Invalid command!")
print("Adios!")
