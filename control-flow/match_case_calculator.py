num1 = int(input("Enter your first number:"))
num2 = int(input("Enter your second number:"))
operation = input("Choose the operation (+, -, *, /):.")

match   operation:
    case "+":
        print(num1+num2)
    case "-":
        print(num1-num2)    
    case "*":
        print(num1*num2)
    case "/":
        print(num1/num2)        