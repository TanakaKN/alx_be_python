# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Function to convert Fahrenheit → Celsius
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius → Fahrenheit
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main program logic
def main():
    try:
        user_temp = float(input("Enter the temperature to convert: "))
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return

    user_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    match user_type:
        case "C":
            fan = convert_to_fahrenheit(user_temp)
            print(f"{user_temp}°C is {fan:.2f}°F")  
        case "F":
            cel = convert_to_celsius(user_temp) 
            print(f"{user_temp}°F is {cel:.2f}°C") 
        case _:
            print("Invalid input. Please enter 'C' or 'F'.")

# Entry point
if __name__ == "__main__":
    main()
