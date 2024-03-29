from src.Operator import Operator, UnaryOperator
from src.operators_library import operators


def solve(expression):
    """
    Solves a string of a given mathematical expression in parameters
    :param expression: A string of a mathematical expression
    :return: The result of the expression as a number
    """
    expression = expression.replace(' ', '')
    if len(expression) == 0:
        return 0
    # a list that hold the operators and operands of the expression
    stack = []
    i = 0
    unary_minus = False
    if expression[0] == '-':
        unary_minus = True
        i = 1

    # read the first number with its unary operators
    num, length = read_number(expression, i)
    stack.append(num)
    i += length
    if i<len(expression) and unary_minus and get_operator_obj(expression[i]).priority < 3.5:
        stack[0] *= -1
        unary_minus = False

    # expression loop
    while i < len(expression):
        current_operator = expression[i]
        # if the character is not a binary operator
        if current_operator not in operators:
            raise ValueError("you entered (" + current_operator + ") where an operator was expected")
        if isinstance(get_operator_obj(current_operator), UnaryOperator):
            raise ValueError(
                "you entered a unary operator (" + current_operator + ") where a binary operator was expected")

        # get the matching object of the operator
        current_operator_obj = get_operator_obj(current_operator)

        # calculate all the binary operators in the stack that have higher or equal priority
        while len(stack) > 2 and get_operator_obj(stack[-2]).priority >= current_operator_obj.priority:
            num2 = stack.pop()
            op = stack.pop()
            num1 = stack.pop()
            stack.append(solve_binary_expression(operators[operators.index(op)], num1, num2))

        stack.append(current_operator)
        i += 1

        num, length = read_number(expression, i)
        stack.append(num)
        i += length

    while len(stack) > 1:
        num2 = stack.pop()
        op = stack.pop()
        num1 = stack.pop()

        stack.append(solve_binary_expression(operators[operators.index(op)], num1, num2))

    res = stack[0]
    if unary_minus:
        res *= -1
    return round(res, 8)


def solve_binary_expression(operator: Operator, operand1, operand2):
    """
    Get a binary expression made of two operands and an operator, solve it and return the answer
    """
    return operator.operation(operand1, operand2)


def read_number(expression, i):
    """
    Read the operand and the unary operators around it in a string expression at index i.
    :param expression: A string of a mathematical expression
    :param i: The index in the array of the first character of the number we want to read
    :return: First value: the number we read. Second value: the number of character that compose the operand and unary
    operators in the string
    """

    left_unary_operators = []
    operand_start_index = i
    current_operator = get_operator_obj(expression[i])
    # set the last priority to the smallest limit
    last_priority = -1
    # collect the left unary operators to a list
    # the operators have to be in ascending priority order
    while (i < len(expression) and current_operator is not None and current_operator.priority > last_priority and
           isinstance(current_operator, UnaryOperator) and current_operator.side == 'left'):
        left_unary_operators.append(current_operator)
        last_priority = current_operator.priority
        i += 1
        current_operator = get_operator_obj(expression[i])
    if i >= len(expression):
        raise ValueError("missing an operand at the end of the expression")
    # check sequence of '-' before the operand
    sign = 1
    while expression[i] == '-':
        sign *= -1
        i += 1
    # find the end index of the number
    if expression[i] == '(':
        close_parentheses_index = find_close_parentheses(expression, i)
        result_parentheses = solve(expression[i + 1:close_parentheses_index])
        num = result_parentheses
        i = close_parentheses_index + 1
    else:
        start = i
        while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
            i += 1
        num = expression[start:i]
        if num == '':
            raise ValueError("you entered a '" + expression[i] + "' where a number was expected")
        # check if the scanned string is a number(could have more than one point)
        try:
            num = float(num)
        except ValueError:
            raise ValueError("The number '" + num + "' is not in a correct format")
    num *= sign
    while len(left_unary_operators) > 0:
        num = left_unary_operators.pop().operation(num)
        print("=", num)
    if i < len(expression):
        current_operator = get_operator_obj(expression[i])
        # set the last priority to the biggest limit
        if current_operator is not None:
            last_priority = current_operator.priority + 1
        # apply the left unary operators calculation
        # the operators have to be in ascending priority order
        while (i < len(expression) and current_operator is not None and current_operator.priority <= last_priority and
               isinstance(current_operator, UnaryOperator) and current_operator.side == 'right'):
            last_priority = current_operator.priority
            num = current_operator.operation(num)
            print("=", num)
            i += 1
            if i >= len(expression):
                break
            current_operator = get_operator_obj(expression[i])

    return num, i - operand_start_index


def get_operator_obj(operator_string):
    """
    gets an operator as a string and retrun an Operator Object from the operators list
    param operator_string: an operator as a string
    """
    for op in operators:
        if op == operator_string:
            return op
    return None


def find_close_parentheses(expression, start_index):
    """
    gets an expression and the index of an opening parenthes,
    returns the index of the matching closing parenthes
    """
    count = 0
    for i in range(start_index + 1, len(expression)):
        if expression[i] == ')':
            if count == 0:
                return i
            count -= 1
        if expression[i] == '(':
            count += 1
    raise ValueError("not valid parentheses format")
