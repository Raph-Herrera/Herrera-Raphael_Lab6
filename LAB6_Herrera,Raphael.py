age = int(input("Enter your age: "))
member = input("Are you an active member?: ")
if age >= 1 and age < 18:
    if member == "Yes":
        print("Your fee is 450.00 Php")
    elif member == "No":
        print("Your fee is 650.00 Php")
elif age >= 18 and age <=65:
    if member == "Yes":
        print("Your fee is 550.00 Php")
    elif member == "No":
        print("Your fee is 750.00 Php")
elif age > 65 and age <= 100:
    if member == "Yes":
        print("Your fee is 550.00 Php")
    elif member == "No":
        print("Your fee is 750.00 Php")
else:
    print("Invalid User Input")