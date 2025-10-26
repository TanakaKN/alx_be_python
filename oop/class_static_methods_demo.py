# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method - adds two numbers
    @staticmethod
    def add(a, b):
        return a + b

    # Class method - multiplies two numbers and prints class attribute
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
