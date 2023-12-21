import sys
import os

# Get the parent directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Add the parent directory to sys.path
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Common.constants import todo_gui_storage 
from Common.functions import read_file, write_file
import PySimpleGUI as sg
import time

sg.theme("black")

clock = sg.Text("", key='clock')
label = sg.Text("Type in a To-do")
input_box = sg.InputText(tooltip="Enter a To-do", key='todo')
add_button = sg.Button("Add", size= 7)
add_by_img = sg.Button(
    image_source=os.path.join(current_dir, 'add.png'), 
    size= 10,
    mouseover_colors='lightblue2',
    tooltip="Add button",
    key='Add2'
    )

available_todos = sg.Listbox(
    values=read_file(todo_gui_storage), 
    key='todos', 
    enable_events=True, 
    size=[45, 10]
)

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
complete_by_img = sg.Button(
    image_source=os.path.join(current_dir, 'complete.png'), 
    size= 10,
    mouseover_colors='lightblue2',
    tooltip="Complete button",
    key='Complete2'
    )
exit_button = sg.Button("Exit")

window = sg.Window(
    "My To-Do App", 
    layout=[[clock],
        [label], [input_box, add_button, add_by_img], [available_todos, edit_button, complete_button, complete_by_img], [exit_button]],
    font=('Times New Roman', 20)
)

while True:
    event, values = window.read(timeout=10)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    user_input = values['todo'].strip()
    if user_input == "" and (event not in ['todos', 'Exit']):
        continue

    user_input = user_input + '\n'
    default_todos = read_file(todo_gui_storage)

    match event:
        case 'Add' | 'Add2':
            default_todos.append(user_input.title())
            write_file(default_todos, todo_gui_storage)
            window['todos'].update(values=default_todos)
            window['todo'].update(value='')

        case 'Edit':
            try:
                new_todo_input = values['todos'][0]
                edit_index = default_todos.index(new_todo_input)
                default_todos[edit_index] = user_input.title()
                write_file(default_todos, todo_gui_storage)

                window['todos'].update(values=default_todos)
                window['todo'].update(value='')

            except ValueError as VE:
                print(f'ERROR: {VE}. Please enter a number after edit\n')
            except IndexError as IE:
                print(f'ERROR: {IE}. Please enter a valid index\n')

        case "Complete" | "Complete2":
            try:
                new_todo_input = values['todos'][0]
                complete_index = default_todos.index(new_todo_input)
                default_todos.pop(complete_index)
                write_file(default_todos, todo_gui_storage)
                
                window['todos'].update(values=default_todos)
                window['todo'].update(value='')

            except ValueError as VE:
                print(f'ERROR: {VE}. Please enter a number after complete\n')
            except IndexError as IE:
                print(f'ERROR: {IE}. Please enter a valid index\n')

        case "todos":
            new_todo_input = values['todos'][0].strip()
            window['todo'].update(value=new_todo_input)

        case 'Exit' | sg.WIN_CLOSED:
            print("---Thank you--- \n")
            break

window.close()