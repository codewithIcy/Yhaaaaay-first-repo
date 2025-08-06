#calculator app

def sum(num_1, num_2):
    return num_1 + num_2

def sub(num_1, num_2):
    return num_1 - num_2

def mult(num_1, num_2):
    return num_1 * num_2

def div(num_1, num_2):
    if num_2 == 0:
        return "Error! Division by zero."
    return num_1 / num_2

print("Welcome to my calculator!!\n")

print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = input("Please select your desired action (1-4): ")

try:
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    if choice == "1":
        print(f"The answer to your operation is {sum(num1, num2)}")
    elif choice == "2":
        print(f"The answer to your operation is {sub(num1, num2)}")
    elif choice == "3":
        print(f"The answer to your operation is {mult(num1, num2)}")
    elif choice == "4":
        print(f"The answer to your operation is {div(num1, num2)}")
    else:
        print("Invalid choice. Please select a number from 1 to 4.")

except ValueError:
    print("Invalid input! Please enter numeric values.")
