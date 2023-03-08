from calculator import Calculator

calc = Calculator()


def display_menu():
    print(" ------------------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Stop the program")
    print(" ------------------------")


def format_input():
    numbers_input = input("Enter 2 numbers: ").split()
    if len(numbers_input) == 2:
        numbers = [int(numeric_string) for numeric_string in numbers_input]
        return numbers
    else:
        print("Entered a wrong number of arguments.")
        format_input()


choice = 1
while choice != 0:
    display_menu()
    choice = int(input("Enter choice: "))
    if choice == 0:
        print("Stopping...")
    elif choice == 1:
        numbers = format_input()
        calc.add(numbers[0], numbers[1])
        print(f"Result: {calc.result}")
    elif choice == 2:
        numbers = format_input()
        calc.subtract(numbers[0], numbers[1])
        print(f"Result: {calc.result}")
    elif choice == 3:
        numbers = format_input()
        calc.multiply(numbers[0], numbers[1])
        print(f"Result: {calc.result}")
    elif choice == 4:
        numbers = format_input()
        calc.divide(numbers[0], numbers[1])
        print(f"Result: {calc.result}")
    else:
        print("Please select a number from the menu.")
