operators = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '@': 5, '$': 5, '&': 5, '%': 4, '~': 6, '!': 6}


def main():
    while 1:
        try:
            expression = input_exercise()
        except ValueError as e:
            print(e)
            return
        if expression == "end":
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
    stack = []
    i = 0
    while i < len(expression):
        num, length = read_number(expression, i)
        stack.append(num)
        i += length
        if i >= len(expression):
            break
        current_operator = expression[i]
        if current_operator not in operators:
            raise ValueError("undefined operator: " + current_operator)
        # if we already had an operator
        if len(stack) > 2:
            last_operator = stack[-2]
            # if the power of the last operator is greater or equal to the power of the current operator
            if operators[last_operator] >= operators[current_operator]:
                num2 = stack.pop()
                op = stack.pop()
                num1 = stack.pop()
                # calculation logic here
        stack.append(current_operator)
        i += 1
    return stack


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
    if num == '':
        raise ValueError("you entered a '" + expression[i] + "' where a number was expected")
    try:
        num = float(num)
    except ValueError as e:
        raise ValueError("The number '" + num + "' is not in a correct format")
    # check if the scanned string is a number(could have more than one point)
    return num * sign, i - start


if __name__ == "__main__":
    main()
