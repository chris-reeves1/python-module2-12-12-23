# part 1

age = int(input("Please enter your age: "))

if age >= 18:
    print("You are in category A")
if age >= 16 and age < 18:
    print("You are in category B")
if age < 16:
    print("You are in category C")


age = int(input("Please enter your age: "))

if age >= 18:
    print("You are in category A")
elif age >= 16:
    print("You are in category B")
else:
    print("You are in category C")

# Part 2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Calc options:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Please choose an option (1-4): ")

if choice == "1":
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif choice == "2":
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif choice == "3":
    result = num1 * num2
    print(num1, "x", num2, "=", result)
elif choice == "4":
    if num2 == 0:
        print("Error: division by zero")
    else:
        result = num1 / num2
        print(num1, "/", num2, "=", result)
else:
    print("Error: invalid choice")

# Grades 1

mark = int(input("Enter exam mark (between 1 and 100): "))

if mark < 1 or mark > 100:
    print("Error: marks must be between 1 and 100")
elif mark < 50:
    print("Fail")
elif mark <= 60:
    print("Pass")
elif mark <= 70:
    print("Merit")
else:
    print("Distinction")

# grades 2
mark = int(input("Enter exam mark (between 1 and 100): "))
level = int(input("Enter student level (1 or 2): "))

if mark < 1 or mark > 100:
    print("Error: marks must be between 1 and 100")
elif level == 1:
    if mark < 50:
        print("Fail")
    elif mark <= 60:
        print("Pass")
    elif mark <= 70:
        print("Merit")
    else:
        print("Distinction")
elif level == 2:
    if mark < 40:
        print("Fail")
    elif mark <= 50:
        print("Pass")
    elif mark <= 65:
        print("Merit")
    else:
        print("Distinction")
else:
    print("Invalid level, please enter 1 or 2")



#Pythagoras:

print("1. Calculate side A")
print("2. Calculate side B")
print("3. Calculate side C")

choice = input("Enter your choice: ")

if choice == "1":
    side_b = float(input("Enter length of side B: "))
    side_c = float(input("Enter length of side C: "))
    side_a = (side_c**2 - side_b**2)**0.5
    print("Length of side A is", side_a)
elif choice == "2":
    side_a = float(input("Enter length of side A: "))
    side_c = float(input("Enter length of side C: "))
    side_b = (side_c**2 - side_a**2)**0.5
    print("Length of side B is", side_b)
elif choice == "3":
    side_a = float(input("Enter length of side A: "))
    side_b = float(input("Enter length of side B: "))
    side_c = (side_a**2 + side_b**2)**0.5
    print("Length of side C is", side_c)
else:
    print("Invalid choice, please enter 1, 2, or 3.")