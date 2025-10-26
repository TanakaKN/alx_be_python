# class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method: performs addition, doesn't use the class or instance
    @staticmethod
    def add(a, b):
        return a + b

    # Class method: performs multiplication and shows the class attribute
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Demonstration
# Using the static method
sum_result = Calculator.add(10, 5)
print(f"The sum is: {sum_result}")

# Using the class method
product_result = Calculator.multiply(10, 5)
print(f"The product is: {product_result}")
