# Asking the user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Using a for loop to generate the table from 1 to 10
for i in range(1, 11):  # range(1, 11) means numbers 1 through 10
    result = number * i
    print(f"{number} x {i} = {result}")
