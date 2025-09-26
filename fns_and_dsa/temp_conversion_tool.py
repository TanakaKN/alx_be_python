# Global conversion factors (must use these exact names)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius using the global FAHRENHEIT_TO_CELSIUS_FACTOR.
    Formula: (F - 32) * 5/9
    """
    # read the global factor (no 'global' statement required for reading)
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit using the global CELSIUS_TO_FAHRENHEIT_FACTOR.
    Formula: (C * 9/5) + 32
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    # Prompt must match assignment example exactly
    user_temp_str = input("Enter the temperature to convert: ")
    # If the user enters a non-numeric value we MUST raise ValueError with this message
    try:
        user_temp = float(user_temp_str)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    user_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if user_type == "C":
        result = convert_to_fahrenheit(user_temp)
        # Print without rounding so test can compare full float representation if needed
        print(f"{user_temp}°C is {result}°F")
    elif user_type == "F":
        result = convert_to_celsius(user_temp)
        print(f"{user_temp}°F is {result}°C")
    else:
        # Raise a ValueError for invalid unit input so tests detect it
        raise ValueError("Invalid unit. Please enter 'C' or 'F'.")

if __name__ == "__main__":
    main()
