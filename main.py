default_todos = []

while True :
    user_msg = input("Enter add, show, edit or exit:- ")
    user_msg = user_msg.strip()     # used to remove leading and trailing whitespace

    match user_msg:
        case 'add':
            user_input = input("Enter a todo:- ").strip()
            default_todos.append(user_input)
        case "show":
            print("Todos are:-")
            for (index, todo) in enumerate(default_todos):
                print(f'{index + 1}--{todo}')
        case 'edit':
            user_input = int(input("Enter the index:- "))
            default_todos[user_input-1] = input("Enter the edited todo:- ")
        case "complete":
            user_input = int(input("Enter the completed index:- "))
            default_todos.pop(user_input-1)
        case "exit":
            print("---Thank you--- \n")
            break
        case _:
            print("Wrong input, Please try again")
    print('\n')