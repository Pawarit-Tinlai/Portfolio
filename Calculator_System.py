def calculate(a, b, operator):
    try:
        a = float(a)
        b = float(b)

        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                return "Error: Division by zero"
            return a / b
        else:
            return "Invalid operator"
    except ValueError:
        return "Invalid number"


# Example
print(calculate(10, 5, "+"))
print(calculate(10, 0, "/"))
