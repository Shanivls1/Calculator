operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '@': 5, '$': 5, '&': 5, '%': 4, '~': 6, '!': 6}


def main():
    while 1:
        try:
            expression = input_exercise()
        except ValueError as e:
            print(e)
            return
        if expression is "end":
            break
        try:
            print(solve(expression))
        except ValueError as e:
            print(e)
    print("closing the program...")


def input_exercise():
    print("Calculator:\n\tsupported operators:\n\t+ : addition\n\t- : subtraction\n\t* : multiplication\n\t/ : "
          "division\n\t^ : power\n\t@ : average\n\t$ : maximum\n\t& : minimum\n\t% : modulo\n\t~ : "
          "negative\n\t! : factorial\n-To end the program enter: 'end'\n")
    exercise = input("Enter an expression to calculate:\n")
    if exercise == 'end':
        return "end"

    return exercise


def solve(expression):
    operands = []
    op = []
    i = 0
    while i < len(expression):
        num, length = read_number(expression, i)
        operands.append(num)
        i += length
        if i >= len(expression):
            break
        if expression[i] not in operators:
            raise ValueError("undefined operator: " + expression[i])
        op.append(expression[i])
        i += 1
    return op, operands


def read_number(expression, i):
    sign = 1
    start = i
    # check '~' before the operand
    if expression[i] == '~':
        sign = -1
        i += 1
    # check sequence of '-' before the operand
    while expression[i] == '-':
        sign *= -1
        i += 1
    # find the end index of the number
    start = i
    while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
        i += 1
    num = expression[start:i]
    try:
        num = float(num)
    except ValueError as e:
        raise ValueError("missing a number")
    # check if the scanned string is a number(could have more than one point)
    return num * sign, i - start


if __name__ == "__main__":
    main()
