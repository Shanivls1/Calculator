import math

from src.Operator import Operator, UnaryOperator

operators = []


# addition operator
def addition_operation(x, y):
    return x + y


operators.append(Operator('+', 1, addition_operation))


# subtraction operator
def subtraction_operation(x, y):
    return x - y


operators.append(Operator('-', 1, subtraction_operation))


# multiplication operator
def multiplication_operation(x, y):
    return x * y


operators.append(Operator('*', 2, multiplication_operation))


# division operator
def division_operation(x, y):
    if y == 0 and x != 0:
        raise ValueError("dividing by zero")
    return x / y


operators.append(Operator('/', 2, division_operation))


# pow operator
def pow_operation(x, y):
    try:
        value = math.pow(x, y)
        return value
    except ValueError as e:
        raise ValueError("imaginary number!")


operators.append(Operator('^', 3, pow_operation))


# average operator
def average_operation(x, y):
    return (x + y) / 2


operators.append(Operator('@', 5, average_operation))


# maximum operator
def maximum_operation(x, y):
    return max(x, y)


operators.append(Operator('$', 5, maximum_operation))


# minimum operator
def minimum_operation(x, y):
    return min(x, y)


operators.append(Operator('&', 5, minimum_operation))


# modulo operator
def modulo_operation(x, y):
    return x % y


operators.append(Operator('%', 4, modulo_operation))


# negative operator
def negative_operation(x):
    return x * -1


operators.append(UnaryOperator('~', 6, negative_operation, 'left'))


# factorial operator
def factorial_operation(x):
    if not isinstance(x, (int, float)):
        raise ValueError("Input must be an integer or a float.")
    if x != int(x) or x < 0:
        raise ValueError("Factorial is defined only for non-negative integers.")
    x = int(x)
    if x < 1:
        return 1
    num = 1.0
    for i in range(1, x + 1):
        num *= i
        if math.isinf(num):
            raise ValueError("number is too large")
    return num


operators.append(UnaryOperator('!', 6, factorial_operation, 'right'))


# sum digits operator
def sum_digits_operation(x):
    string_x = (str(x)).replace('.', '')
    sum_digits = 0
    for digit in string_x:
        if digit == 'e':
            return sum_digits
        sum_digits += int(digit)
    return sum_digits


operators.append(UnaryOperator('#', 6, sum_digits_operation, 'right'))


def unary_minus(x):
    return x * -1


operators.append(UnaryOperator('-*', 3.5, unary_minus, 'left'))
