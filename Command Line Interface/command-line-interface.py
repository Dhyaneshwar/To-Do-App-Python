import sys
import os

# Get the parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Add the parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from constants import todo_cli_storage 
from functions import read_file, write_file

while True :
    user_msg = input("Enter add, show, edit, complete or exit:- ")
    user_msg = user_msg.strip()     # used to remove leading and trailing whitespace

    user_action = user_msg.split(' ')[0].strip()
    match user_action:
        case 'add' | 'new':
            user_input = user_msg.split(' ', 1)[1].strip() + '\n'
            # Appending the newly added data to file
            with open(todo_cli_storage, 'a') as file:
                file.writelines(user_input)

        case "show":
            print("Todos are:-")
            default_todos = read_file()
            new_todos = [todo.strip('\n') for todo in default_todos]
            for (index, todo) in enumerate(new_todos):
                print(f'{index + 1}--{todo.title()}')

        case 'edit':
            try:
                user_input = int(user_msg.split(' ', 1)[1].strip())
                default_todos = read_file()
                default_todos[user_input-1] = input("Enter the edited todo:- ") + "\n"
                write_file(default_todos)
            except ValueError as VE:
                print(f'ERROR: {VE}. Please enter a number after edit\n')
            except IndexError as IE:
                print(f'ERROR: {IE}. Please enter a valid index\n')

        case "complete":
            try:
                user_input = int(user_msg.split(' ', 1)[1].strip())
                default_todos = read_file()
                default_todos.pop(user_input-1)
                write_file(default_todos)
            except ValueError as VE:
                print(f'ERROR: {VE}. Please enter a number after complete\n')
            except IndexError as IE:
                print(f'ERROR: {IE}. Please enter a valid index\n')

        case "exit":
            print("---Thank you--- \n")
            break

        case _:
            print("Wrong input, Please try again")