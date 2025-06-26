print("welcome to the Starbucks app!")

name = input("please enter a name for the order: ")
time = input("please enter the current time: ")
date = input("please enter the current date: ")

menu = {
    "pink drink": 5.25,
      "strawberry acai": 5.25, 
        "summer-berry lemonade": 6.25
        }

print("------menu------")
print("~~~~~~~~~~~~~~~~")
for item in menu:
    print(f"{item}: {menu[item]}")
      
customizations = {
    "light ice": 0, 
    "light lemonade": 0, 
    "syrups": 1.25, 
    "cold foam": 1.25, 
    "sweet cream": 1.25
    }
print("customizations: ")
for item in customizations:
    print(f"{item}: {customizations[item]}")

cart_total = 0
cart = []

while True:
    size = input("please select a size: (grande, venti, trenta): ").lower()
    if size == "grande":
        size_price = 0.00
    elif size == "venti":
        size_price = 0.50
    elif size == "trenta":
        size_price = 1.00
    else:
        print("Invalid size. Defaulting to grande")

    drink_choice = input("Please select your drink: ").lower()
    if drink_choice == "pink drink":
        drink_price = 5.25
    elif drink_choice == "strawberry acai":
        drink_price = 5.25
    elif drink_choice == "summer-berry lemonade":
        drink_price = 6.25
    else:
        print("Invalid drink. Defaulting to Strawberry Acai.")
        drink_choice = "strawberry acai lemonade"
        drink_price = 5.25

    customization_choice = input("Please choose a customization or press enter to skip: ").lower()
    if customization_choice == "light ice":
        customization_price = 0
    elif customization_choice == "light lemonade":
        customization_price = 0
    elif customization_choice == "syrups":
        customization_price = 1.25
    elif customization_choice == "cold foam":
        customization_price = 1.25
    elif customization_choice == "sweet cream":
        customization_price = 1.25
    else:
        customization_choice = "no customizations"
        customization_price = 0

    item_total = drink_price + size_price + customization_price
    cart_total += item_total
    cart.append(f"{size} {drink_choice} with {customization_choice} : ${item_total}")

    again = input("keep ordering? (yes or no): ").lower()
    if again == "no":
        break
        
print("-----Order Summary-----")
print(f"{name}")
for item in cart:
    print(item)
print("---------------------------------")
print("Mobile")
print("---------------------------------")
print(f"{time}")
print(f"{date}")
print(f"Total: ${cart_total}")