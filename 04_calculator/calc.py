from chunk_def import addition, subtract, divide, multiply


def main():
    while True:
        print("Welcome to the calculator app.")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit the app")

        operation = input("What operations do you want to perform? ")

        if operation == "1":
            numbers = input("Enter all the numbers separated by commas to add: ")
            numbers_list = numbers.split(",")
            addition(*numbers_list)
        elif operation == "2":
            print("Lets start a-b format")
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))

            subtract(a, b)
        elif operation == "3":
            numbers = input("Enter all the numbers separated by commas to add: ")
            numbers_list = numbers.split(",")
            multiply(*numbers_list)
        elif operation == "4":
            print("Lets start a/b format")
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            divide(a, b)
        elif operation == "5":
            break
        else:
            print("Invalid choice! Lets try again")
            continue


if __name__ == "__main__":
    main()
