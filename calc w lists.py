check = True  # This controls the while loop

while check:
   
    print("\nChoose an option:")
    print("1) addition")
    print("2) subtraction")
    print("3) multiplication")
    print("4) division")
    print("5) modular division")
    print("6) quit")

    option = input("Enter the number or name of the operation: ").lower()

 
    if option == "6" or option == "quit":
        check = False
        print("Goodbye!")
    
   
    elif option in ["1", "addition", "2", "subtraction", "3", "multiplication", "4", "division", "5", "modular division"]:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if option == "1" or option == "addition":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        
        elif option == "2" or option == "subtraction":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")

        elif option == "3" or option == "multiplication":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")

        elif option == "4" or option == "division":
            if num2 == 0:
                print("Error: Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")

        elif option == "5" or option == "modular division":
            if num2 == 0:
                print("Error: Cannot mod by zero.")
            else:
                result = num1 % num2
                print(f"{num1} % {num2} = {result}")

    else:
        print("Invalid option. Please try again.")
