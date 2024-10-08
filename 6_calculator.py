def calculator(operator):
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Error: Division by zero."
        return x / y

    match operator:
        case "+":
            return add
        case "-":
            return subtract
        case "*":
            return multiply
        case "/":
            return divide
        case _:
            return lambda x, y: "Error: Operator not supported."


add = calculator('+')
subtract = calculator('-')
multiply = calculator('*')
divide = calculator('/')
another_operator = calculator("^^")

# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))
# print(another_operator(1, 2))
