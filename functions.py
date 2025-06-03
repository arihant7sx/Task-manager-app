FILEPATH = "tasks.txt"


def get_tasks(filepath=FILEPATH):
    """ Reads a text file and
    returns the list of tasks
     """
    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()
    return tasks_local


def write_tasks(tasks_arg, filepath=FILEPATH):
    """ Write the tasks in tasks list"""
    with open(filepath, 'w') as file:
        file.writelines(tasks_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_tasks())