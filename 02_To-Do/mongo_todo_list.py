# Create Menu where user can see options
# View, Add, Update, Delete, and Close the application

import pymongo

from bson import ObjectId

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["todo_database"]

collection = db["todos"]

print(collection)

def list_todos():
    all_todo = collection.find()
    print("-" * 70)
    todo_count = collection.count_documents(filter={})
    if todo_count > 0:
        for todo in all_todo:
            print(f"ID: {todo["_id"]}, Title: {todo["title"]}, Description: {todo['desc']}")
    else:
        print("No TODOs found. Consider adding a new one.")
    print("-" * 70)

def add_todo(title, desc):
    collection.insert_one({"title":title,"desc":desc})
    print("-" * 70)
    print("TODO added successfully")
    print("-" * 70)


def update_todo(todo_id, title, desc):
    collection.find_one_and_update(
        {"_id":ObjectId(todo_id)},
        {"$set":{"title":title,"desc":desc}},
    )
    print("-" * 70)
    print(f"TODO with {todo_id} updated successfully")
    print("-" * 70)

def delete_todo(todo_id):
    collection.find_one_and_delete({"_id":ObjectId(todo_id)})
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
