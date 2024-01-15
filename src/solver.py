from operators_library import operators
from src.Operator import Operator, UnaryOperator


def solve(expression):
    """
    Solves the mathematical expression in parameters
    :param expression: A string of a mathematical expression
    :return: The result of the expression
    """
    # a list that hold the operators and operands of the expression
    stack = []
    """
    loop that go over the expression
    each iteration read an operand and calculate it with its unary operators, and the operator that follow him
    then calculate all the binary expression before him that's operator's priority is smaller or equal to the current
    operator's priority
    """
    i = 0
    while i < len(expression):
        if expression[i] == '(':
            close_parentheses_index = find_close_parentheses(expression, i)
            result_parentheses = solve(expression[i + 1:close_parentheses_index])
            stack.append(result_parentheses)
            i = close_parentheses_index+1
        else:
            num, length = read_number(expression, i)
            stack.append(num)
            i += length

        # if it was the last number
        if i >= len(expression):
            break

        current_operator = expression[i]

        # if the character that comes after the number in not an accepted operator
        if current_operator not in operators:
            raise ValueError("undefined operator: " + current_operator)

        # find the priority of the current operator
        current_operator_obj = get_operator_obj(current_operator)

        # if there's an operator in the stack and its priority is higher or equal to the priority of the current
        while len(stack) > 2 and get_operator_obj(stack[-2]).priority >= current_operator_obj.priority:
            num2 = stack.pop()
            op = stack.pop()
            num1 = stack.pop()
            stack.append(solve_binary_expression(operators[operators.index(op)], num1, num2))

        stack.append(current_operator)

        i += 1

    while len(stack) > 1:
        num2 = stack.pop()
        op = stack.pop()
        num1 = stack.pop()

        stack.append(solve_binary_expression(operators[operators.index(op)], num1, num2))
    if len(stack)==0:
        raise ValueError("please enter an expression")
    return stack[0]


def solve_binary_expression(operator: Operator, operand1, operand2):
    return operator.operation(operand1, operand2)


def read_number(expression, i):
    """
    Read the number in a string expression at index i.
    :param expression: A string of a mathematical expression
    :param i: The index in the array of the first character of the number we want to read
    :return: First value: the number we read. Second value: the number of character that compose the number in the string
    """
    left_unary_operators = []
    # keep the index of start of the operand
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
        raise ValueError("idk!!!1")
    # check sequence of '-' before the operand
    sign = 1
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
    # check if the scanned string is a number(could have more than one point)
    try:
        num = float(num)
    except ValueError:
        raise ValueError("The number '" + num + "' is not in a correct format")
    num *= sign
    while len(left_unary_operators) > 0:
        num = left_unary_operators.pop().operation(num)
    if i < len(expression):
        current_operator = get_operator_obj(expression[i])
        # set the last priority to the biggest limit
        last_priority = current_operator.priority + 1
        # apply the left unary operators calculation
        # the operators have to be in ascending priority order
        while (i < len(expression) and current_operator is not None and current_operator.priority < last_priority and
               isinstance(current_operator, UnaryOperator) and current_operator.side == 'right'):
            current_operator = get_operator_obj(expression[i])
            last_priority = current_operator.priority
            num = current_operator.operation(num)
            i += 1


    return num, i - operand_start_index


def get_operator_obj(operator_string):
    for op in operators:
        if op == operator_string:
            return op
    return None


def find_close_parentheses(expression, start_index):
    count = 0
    for i in range(start_index + 1, len(expression)):
        if expression[i] == ')':
            if count == 0:
                return i
            count -= 1
        if expression[i] == '(':
            count += 1
    raise ValueError("not valid parentheses format")
