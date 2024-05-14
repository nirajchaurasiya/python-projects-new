# Create Menu where user can see options
# View, Add, Update, Delete, and Close the application

todos = []

def list_todos():
    print("-" * 70)
    if len(todos) > 0:
        for todo in todos:
            print(f"ID: {todo["id"]}, Title: {todo["title"]}, Description: {todo['desc']}")
    else:
        print("No TODOs found. Consider adding a new one.")
    print("-" * 70)

def add_todo(title, desc):
    todos.append({"id":len(todos)+1,"title":title,"desc":desc})
    print("-" * 70)
    print("TODO added successfully")
    print("-" * 70)


def update_todo(todo_id, title, desc):
    todos[int(todo_id)-1] = {"id":len(todos)+1 ,"title":title,"desc":desc}
    print("-" * 70)
    print(f"TODO with {todo_id} updated successfully")
    print("-" * 70)

def delete_todo(todo_id):
    del todos[int(todo_id)-1]
    print("-" * 70)
    print(f"TODO with ID {todo_id} deleted successfully")
    print("-" * 70)


def main():
    while True:

        print("Welcome to the command line TO-DO application.")
        print("1. View all TODOs")
        print("2. Add a new TODO")
        print("3. Update a TODO")

        print("4. Delete a TODO")
        print("5: Close the application")
        print("-" * 50)

        choice = input("Enter your choice: ")

        if choice == "1":
            list_todos()

        elif choice == "2":
            title = input("Enter the title: ")
            desc = input("Enter the description: ")
            add_todo(title, desc)

        elif choice == "3":
            list_todos()
            todo_id = input("Enter the todo id to be updated: ")
            title = input("Enter the updated title: ")
            desc = input("Enter the updated description: ")
            update_todo(todo_id, title, desc)

        elif choice == "4":
            list_todos()
            todo_id = input("Enter the todo id to be deleted: ")
            delete_todo(todo_id)

        elif choice == "5":
            print("Have a nice day!😊")
            break

        else:
            print("-" * 50)
            print("You entered an invalid option. Please try again.")
            print("-" * 50)
            continue


if __name__ == "__main__":
    main()
