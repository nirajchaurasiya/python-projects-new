def addition(*args):
    add = 0
    for item in args:
        add += int(item)
    print(f"Sum = {add}")


def subtract(a, b):
    print(f"{a} - {b} = {a - b}")


def multiply(*args):
    multiplication = 1
    for item in args:
        multiplication *= int(item)
    print(f"Multiplication = {multiplication}")


def divide(a, b):
    print(f"{a} / {b} = {a / b}")
