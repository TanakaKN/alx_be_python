class SimpleCalculate:
    print("A simple calculator class that supports basic arithmetic operations.")

    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a*b
    
    def divide(a, b):
        if b == 0:
            return "Error: Cannot divide by zero."
        return a / b
    
    