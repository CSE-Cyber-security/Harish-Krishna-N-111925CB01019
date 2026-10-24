"""Simple command-line calculator."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number, please try again.")


def main():
    print("Simple Calculator")
    print("Operations: + - * /   (type 'q' at the operator prompt to quit)")

    while True:
        op = input("\nOperator (+, -, *, /) or q to quit: ").strip()
        if op.lower() == "q":
            print("Goodbye!")
            break
        if op not in OPERATIONS:
            print("Unknown operator. Please use +, -, * or /.")
            continue

        a = read_number("First number: ")
        b = read_number("Second number: ")

        try:
            result = OPERATIONS[op](a, b)
            print(f"{a:g} {op} {b:g} = {result:g}")
        except ValueError as err:
            print(f"Error: {err}")


if __name__ == "__main__":
    main()
