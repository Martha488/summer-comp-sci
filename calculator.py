num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined (division by zero)"
modulus = num1 % num2 if num2 != 0 else "undefined (mod by zero)"
print(f"\nHere are your results:")
print(f"Sum: {num1} + {num2} = {addition}")
print(f"Difference: {num1} - {num2} = {subtraction}")
print(f"Product: {num1} * {num2} = {multiplication}")
print(f"Quotient: {num1} / {num2} = {division}")
print(f"Remainder: {num1} % {num2} = {modulus}")