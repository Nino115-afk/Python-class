while True:
    print("1, Sum")
    print("2, sub")
    print("3, mul")
    print("4, div")
    print("0, exit")
    op = int(input("Enter your option: "))
    if op == 1:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        sum = num1 + num2
        print("sum is: ", sum)
    elif op == 2:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        sub = num1 - num2
        print("sub is : ", sub)
    elif op == 3:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        mul = num1 * num2
        print("mul is: ", mul)
    elif op == 4:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if num2 != 0:
            div = num1 / num2
            print("div is: ", div)
        else:
            print("Error: Division by zero is not allowed.")
    elif op == 0:
        print("Exiting the program.")
        break