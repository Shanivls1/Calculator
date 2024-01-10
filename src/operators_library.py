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
    return x / y


operators.append(Operator('/', 1, division_operation))


# pow operator
def pow_operation(x, y):
    return x ** y


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
    num = 1
    for i in range(1, x + 1):
        num = num * i
    return num


operators.append(UnaryOperator('!', 6, factorial_operation, 'right'))


# sum digits operator
def sum_digits_operation(x):
    num = 0
    while x != 0:
        num = num + x % 10
        x = x // 10
    return num


operators.append(UnaryOperator('#', 6, sum_digits_operation, 'right'))
