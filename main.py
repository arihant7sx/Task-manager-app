tasks = []
while True:
    user_choice = input("Type add, show, edit, complete or exit")

    match user_choice.strip():
        case 'add':
            task = input("enter a task")
            tasks.append(task)
        case 'show' :
            for index,item in enumerate(tasks):
                item=item.title()
                print(f"{index+1}-{item}")
        case 'edit':
            number = int(input("number of the task to edit: "))
            number = number - 1
            new_task = input("Enter the new task")
            tasks[number] = new_task
        case 'complete':
            number=int(input("Enter the number of the completed task"))
            tasks.pop(number-1)

        case 'exit':
            break

print("Adios!,")
