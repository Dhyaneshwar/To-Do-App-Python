default_todos = []
run_loop = True
while True :
    user_msg = input("Enter a add, edit, show or exit:- ")
    print('Value entered by the user is {}'.format(user_msg))

    match user_msg:
        case 'add':
            user_input = input("Enter a todo:- ")
            default_todos.append(user_input)
        case 'edit':
            user_input = int(input("Enter the index:- "))
            default_todos[user_input] = input("Enter the edited todo:- ")
        case "show":
            print("todos are:-")
            for (index, todo) in enumerate(default_todos):
                print(f'{index + 1}.{todo}')
        case "exit":
            print("---Thank you---")
            break
        case _:
            print("Wrong input, Please try again")