import gui
import mat
import db


def main_but():
    db.num_1 = gui.enter_number()
    op = gui.operation()
    db.num_2 = gui.enter_number()
    match op:
        case '+':
            return mat.sum_numbers(db.num_1, db.num_2)
        case '-':
            return mat.dif_numbers(db.num_1, db.num_2)
        case '*':
            return mat.mul_numbers(db.num_1, db.num_2)
        case _:
            return mat.dev_numbers(db.num_1, db.num_2)


gui.print_result()
