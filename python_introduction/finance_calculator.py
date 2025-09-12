monthly_income = int(input("Enter your monthly income: "))  # Renamed variable
monthly_expenses = int(input("Enter your total monthly expenses: "))  # Renamed variable

monthly_savings = monthly_income - monthly_expenses  # Matches the required pattern

annual_interest_rate = 0.05

Projected_Savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

print(f"Your monthly savings are ${monthly_savings}.")

print(f"Projected savings after one year, with interest, is: ${Projected_Savings}")