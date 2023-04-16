print("Welcome to my Mad Libs Generator")
name = input("Enter Your Name: ")
age = input("Enter Your Age: ")
fav_food = input("Your Favorite Food is: ")
print()
if age.isnumeric():
    print("Hello, My name is", name.capitalize())
    print("I am", age, "years old")
    print("My favourite food is",fav_food.capitalize())
else:
    print("Invalid!!!!!!!")
