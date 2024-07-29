def get_todos():
    with open('todos.txt', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


while True:
    user_action = input("Type add, edit, complete, show or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:].title()

        # File handling method1
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        # File handling method2
        todos = get_todos()
        todos.append(todo)

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos()
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo.title() + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        except ValueError:
            print("Error! Command not valid!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        except IndexError:
            print("There is not item with that number!")
            continue

    elif user_action.startswith("exit"):
        break

    else:
        print("Command not valid")

print("Bye!")
