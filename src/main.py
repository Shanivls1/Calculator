operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '@': 5, '$': 5, '&': 5, '%': 4, '~': 6, '!': 6}
unary = ['~', '!']


def main():
    """
    An advance calculator program that input mathematical expression of the user until he enter 'end' and print the
    result of the expression
    """
    while 1:
        # explanation message
        print("Calculator:\n\tsupported operators:\n\t+ : addition\n\t- : subtraction\n\t* : multiplication\n\t/ : "
              "division\n\t^ : power\n\t@ : average\n\t$ : maximum\n\t& : minimum\n\t% : modulo\n\t~ : "
              "negative\n\t! : factorial\n-To end the program enter: 'end'\n")
        expression = input("Enter an expression to calculate:\n")

        if expression == 'end':
            break

        try:
            print(solve(expression))
        except ValueError as e:
            print(e)

    print("closing the program...")


def solve(expression):
    """
    Solves the mathematical expression in parameters
    :param expression: A string of a mathematical expression
    :return: The result of the expression
    """
    # a list that till hold the elements of the expression
    stack = []

    i = 0
    while i < len(expression):
        num, length = read_number(expression, i)
        stack.append(num)

        i += length
        # if an operator don't appear after the number(end of the expression)
        if i >= len(expression):
            break

        current_operator = expression[i]

        # if the character that comes after the number in not an accepted operator
        if current_operator not in operators or current_operator in unary:
            raise ValueError("undefined operator: " + current_operator)

        # if we there's an operator in the stack and its priority is higher or equal to the priority of the current
        while len(stack) > 2 and operators[stack[-2]] >= operators[current_operator]:
            num2 = stack.pop()
            op = stack.pop()
            num1 = stack.pop()
            stack.append(solve_binary_expression(num1, op, num2))

        stack.append(current_operator)

        i += 1

    while len(stack) > 1:
        num2 = stack.pop()
        op = stack.pop()
        num1 = stack.pop()

        stack.append(solve_binary_expression(num1, op, num2))

    return stack[0]


def read_number(expression, i):
    """
    Read the number in a string expression at index i.
    :param expression: A string of a mathematical expression
    :param i: The index in the array of the first character of the number we want to read
    :return: First value: the number we read. Second value: the number of character that compose the number in the string
    """
    base_start = i
    sign = 1
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
    if num == '':
        raise ValueError("you entered a '" + expression[i] + "' where a number was expected")
    try:
        num = float(num)
    except ValueError as e:
        raise ValueError("The number '" + num + "' is not in a correct format")
    # check if the scanned string is a number(could have more than one point)
    return num * sign, i - base_start


def solve_binary_expression(num1, op, num2):
    """
    Solves a binary expression (an expression that contain operands and one operator)
    :param num1: The first operand of the expression
    :param op: The operator of the expression
    :param num2: The second operand of the expression
    :return: The result of the expression
    """
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        if num2 == 0:
            raise ValueError("division by zero")
        return num1 / num2
    elif op == '^':
        return num1 ** num2
    elif op == '@':
        return (num1 + num2) / 2
    elif op == '$':
        return max(num1, num2)
    elif op == '&':
        return min(num1, num2)
    elif op == '%':
        return num1 % num2


if __name__ == "__main__":
    main()
