def perform_operation(num1:float,num2:float,operation:str):
    match operation:
        case "subtract":
            results = num1 - num2
        case "add":
            results = num1+num2
        case "multiply":
            results = num1 * num2
        case "division":
            if num2 != 0:
                results = num1/num2
            else:
                return "Error: Division by zero is not allowed."
        case _:
            return "Error: Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'division'."
    return results    
