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

    user_action = user_msg.split(' ')[0].strip()
    match user_action:
        case 'add' | 'new':
            user_input = user_msg.split(' ', 1)[1].strip() + '\n'
            # Appending the newly added data to file
            with open(todo_storage, 'a') as file:
                file.writelines(user_input)

        case "show":
            print("Todos are:-")
            default_todos = read_file(todo_storage)
            new_todos = [todo.strip('\n') for todo in default_todos]
            for (index, todo) in enumerate(new_todos):
                print(f'{index + 1}--{todo.title()}')

        case 'edit':
            try:
                user_input = int(user_msg.split(' ', 1)[1].strip())
                default_todos = read_file(todo_storage)
                default_todos[user_input-1] = input("Enter the edited todo:- ") + "\n"
                write_file(todo_storage, default_todos)
            except ValueError as VE:
                print(f'ERROR: {VE}. Please enter a number after edit\n')
            except IndexError as IE:
                print(f'ERROR: {IE}. Please enter a valid index\n')

        case "complete":
            try:
                user_input = int(user_msg.split(' ', 1)[1].strip())
                default_todos = read_file(todo_storage)
                default_todos.pop(user_input-1)
                write_file(todo_storage, default_todos)
            except ValueError as VE:
                print(f'ERROR: {VE}. Please enter a number after complete\n')
            except IndexError as IE:
                print(f'ERROR: {IE}. Please enter a valid index\n')

        case "exit":
            print("---Thank you--- \n")
            break

        case _:
            print("Wrong input, Please try again")