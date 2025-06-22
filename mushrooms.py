#mushrooms:
#large mushrooms = size greater than 1000
#small mushrooms = size less than 100
#medium mushrooms = all other mushrooms

mushrooms = []
check = True
while check:
    option = input("Enter mushroom weight or type STOP: ")

    if option == "STOP":
        check = False

    elif int(option) < 1:
        print("Weight must be bigger than zero!")

    else:
        mushrooms.append(int(option))
    
small = 0
medium = 0
large = 0
for mushroom in mushrooms:
    if mushroom > 1000:
        large +=1
    elif mushroom < 100:
        small += 1
    else:
        medium += 1

print(f"All mushroom weights: {mushrooms}")
print(f"There were: {small} small mushrooms")
print(f"There were: {medium} medium mushrooms")
print(f"There were: {large} large mushrooms")