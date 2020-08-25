
# import RockPaperScissors


def calc():
    while True:
        try:
            num1 = float(input("Please enter a number: "))
            op = input("Enter an operator: ")
            num2 = float(input("Please enter another number: "))
            if op == "+" or op == "plus":
                print(num1 + num2)
                break
            elif op == "-" or op == "minus":
                print(num1 - num2)
                break
            elif op == "/" or op == "divide":
                print(num1 / num2)
                break
            elif op == "*" or op == "times":
                print(num1 * num2)
                break
            else:
                print("Enter a valid operator...")
        except ValueError:
            print("Try again....")


calc()
