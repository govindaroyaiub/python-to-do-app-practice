todos = []

while True:
    user_action = input("Type add, edit, delete, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)

        case 'show' | 'display':
            length = len(todos)
            if length == 0:
                print("Hey, you have not added any todos yet!")
            else:
                for index, value in enumerate(todos):
                    index = index + 1
                    item = value.title()
                    print(index, ".", item)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

        case 'delete' | 'remove':
            length = len(todos)
            if length == 0:
                print("Hey, you have not added any todos yet!")
            else:
                for index, value in enumerate(todos):
                    index = index + 1
                    item = value.title()
                    print(index, ".", item)

                number = int(input("Enter the number to delete the task:"))
                todos.pop(number - 1)

        case 'exit':
            break

print("Bye!")