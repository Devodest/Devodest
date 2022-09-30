import db
import controller


def enter_number():
    while True:
        try:
            number = int(input('Enter number: '))
            return number
        except ValueError:
            print("Entered value can't be a number")


def operation():
    while True:
        op = input('Enter operation: ')
        if (op == "+") or (op == "-") or (op == "*") or (op == "/"):
            return op
        else:
            print("'Entered value can't")


def print_result():
    db.result = controller.main_but()
    print(db.result)
