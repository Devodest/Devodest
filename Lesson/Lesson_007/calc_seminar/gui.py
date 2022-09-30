def get_info():
    number_a = input("Enter first number: ")
    equation = input('Enter equation: ')
    number_b = input("Enter second number: ")
    numbers = number_a + ' ' + equation + ' ' + number_b
    return numbers


def send_info(a):
    print(f'Your result: {a}')
