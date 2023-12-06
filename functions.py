from constants import todo_storage 

def read_file(file_loc = todo_storage):
    with open(file_loc, 'r') as file:
        content = file.readlines()
        return content
    
def write_file(content, file_loc=todo_storage):
    with open(file_loc, 'w') as file:
        file.writelines(content)

if __name__ == '__main__':
    print(read_file())