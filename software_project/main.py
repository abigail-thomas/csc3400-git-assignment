from calculator import *


def main():
    print("ADD, SUBTRACT, MULTIPLY, DIVIDE, POWER, SQUARE ROOT")
    user_choice = input("From the above options, what operation would you like to use? ").upper()
    try:
        # one input
        if user_choice == "SQAURE ROOT":
            num = input("Enter a number: ")
            print(square_root(int(num)))
        
        elif user_choice in ("ADD, SUBTRACT, MULTIPLY, DIVIDE, POWER"):
            n1 = input("Enter first number: ")
            n2 = input("Enter second number: ")

            match user_choice:
                case "ADD":
                    print(add(int(n1), int(n2)))
                case "SUBTRACT":
                    print(subtract(int(n1), int(n2)))
                case "MULTIPLY":
                    print(multiply(int(n1), int(n2)))
                case "DIVIDE":
                    print(divide(int(n1), int(n2)))
                case "POWER":
                    print(power(int(n1), int(n2)))

        else:
            print("Sorry, that operation does not yet exist in our system. Please try again :)")

    
    except ValueError:
            print("Invalid input. Please try again.")

    except ZeroDivisionError:
            print("Invalid input for your second number: Can't divide by zero. Please try again.")
    
    except Exception as e:
            print("Error: ", e, ". Please try again.")


