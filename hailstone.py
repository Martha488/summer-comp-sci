num = int(input("Enter your number: "))

while num >= 2:
    if num % 2 == 0:  
        num = num // 2
    else:  
        num = num * 3 + 1

    print(f"The current hailstone's height is: {num}")