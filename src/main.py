from src.solver import solve


def calculate_expression(expression):
    """
    calculate a given expression ,catch the error and print it
    """
    try:
        print(solve(expression))
    except ValueError as e:
        print(e)


def main():
    """
    An advance calculator program that input mathematical expression of the user until he enter 'end' and print the
    result of the expression
    """
    # explanation message
    print("Calculator:\n\tTo end the program enter: 'end'\n")
    while 1:
        try:
            expression = input("Enter an expression to calculate:\n")
        except EOFError:
            print("you entered an incorrect expression: ctrl+d ")
            break

        if expression == 'end':
            break
        calculate_expression(expression)
    print("closing the program...")


if __name__ == "__main__":
    main()
