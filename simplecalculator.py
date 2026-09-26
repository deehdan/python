while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator  = input("Enter an operator: ")

    if (operator == "-"):
        result = num1 - num2
    elif (operator == "+"):
        result = num1 + num2
    elif (operator == "*"):
        result = num1 * num2
    elif ( operator == "/"):
        result = num1 / num2
    else:
        print("Enter a valid operator!")   
        

    print("The answer is: ", result)   

    ans = input("Are you done? y/n: ")
    if (ans == "y"):
        print("Goodbye!")
        break
    