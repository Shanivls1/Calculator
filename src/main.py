from solver import solve


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


if __name__ == "__main__":
    main()
