from constants import todo_storage 

def read_file(file_loc):
    with open(file_loc, 'r') as file:
        content = file.readlines()
        return content
    
def write_file(file_loc, content):
    with open(file_loc, 'w') as file:
        file.writelines(content)

while True :
    user_msg = input("Enter add, show, edit, complete or exit:- ")
    user_msg = user_msg.strip()     # used to remove leading and trailing whitespace

    match user_msg:
        case 'add':
            user_input = input("Enter a todo:- ").strip() + '\n'
            # Appending the newly added data to file
            with open(todo_storage, 'a') as file:
                file.writelines(user_input)

        case "show":
            print("Todos are:-")
            default_todos = read_file(todo_storage)
            for (index, todo) in enumerate(default_todos):
                print(f'{index + 1}--{todo}', end='')

        case 'edit':
            user_input = int(input("Enter the index:- "))
            default_todos = read_file(todo_storage)
            try:
                default_todos[user_input-1] = input("Enter the edited todo:- ")
                write_file(todo_storage, default_todos)
            except IndexError as IE:
                print(f'ERROR: {IE}. Please enter a valid index')

        case "complete":
            user_input = int(input("Enter the completed index:- "))
            default_todos = read_file(todo_storage)
            try:
                default_todos.pop(user_input-1)
                write_file(todo_storage, default_todos)
            except IndexError as IE:
                print(f'ERROR: {IE}. Please enter a valid index')

        case "exit":
            print("---Thank you--- \n")
            break

        case _:
            print("Wrong input, Please try again")
    print('\n')