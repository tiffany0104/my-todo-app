FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todo(todos_arg, filepath=FILEPATH):
    """write a to-do item in the text file."""
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_arg)


if __name__ == "__Main__":
    print(get_todos())
