class Calculator:
    def __init__(self):
        pass

    def addition(self, num1, num2):
        return num1 + num2

    def subtraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2

    def division(self, num1, num2):
        try:
            result = num1 / num2
        except ZeroDivisionError:
            return "Cannot divide by zero"
        return result


def main():
    calc = Calculator()

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter the operator (Add, Subtract, Multiply, Divide): ")
        num2 = float(input("Enter the second number: "))

        if operator not in ["Add", "Subtract", "Multiply", "Divide"]:
            print("Invalid operator. Please enter one of: Add, Subtract, Multiply, Divide")
        else:
            if operator == "Add":
                result = calc.addition(num1, num2)
            elif operator == "Subtract":
                result = calc.subtraction(num1, num2)
            elif operator == "Multiply":
                result = calc.multiplication(num1, num2)
            elif operator == "Divide":
                result = calc.division(num1, num2)

            print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        
main()
