while True:
    print ("\nOptions: ")
    print ("Enter + to add two numbers")
    print ("Enter - to substract two numbers")
    print ("Enter * to multiply two numbers")
    print ("Enter / to divide two numbers")
    print ("Enter 'quit' to close the program")

    user_input = raw_input(":")

    if user_input == "quit":
        break

    elif user_input == "+":
        num1 = float(input("Enter the number: "))
        num2 = float(input("Enter the number: "))
        result = str(num1 + num2)
        print ("the answer is: " + result)

    elif user_input == "-":
        num1 = float(input("Enter the number: "))
        num2 = float(input("Enter the number: "))
        result = str(num1 - num2)
        print ("the answer is: " + result)

    elif user_input == "*":
        num1 = float(input("Enter the number: "))
        num2 = float(input("Enter the number: "))
        result = str(num1 * num2)
        print ("the answer is: " + result)

    elif user_input == "/":
        num1 = float(input("Enter the number: "))
        num2 = float(input("Enter the number: "))
        result = str(num1 / num2)
        print ("the answer is: " + result)

    else:
        print("input unknown")
