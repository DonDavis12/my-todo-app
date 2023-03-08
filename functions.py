#backend
FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """
    Read a text file and return the list of to-do items.
    if you want to print out this documentation: print(help(get_todos))

    These strings can also be used for multiline texts.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath = FILEPATH):
    """ Write to-do items in the text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

print("The functions are imported from:", __name__)     #This part executed when this python file is imported.

if __name__ == "__main__":              #if you want this part of the code to be executed only inside this python file.
    print("Hello from functions!")
