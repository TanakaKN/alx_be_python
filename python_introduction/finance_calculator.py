users_monthly_income = int(input("Enter your monthly income: "))
users_monthly_expenses = int(input("Enter your total monthly expenses: "))

monthly_savings = users_monthly_income - users_monthly_expenses

annual_interest_rate = 0.05

Projected_Savings = (monthly_savings * 12) + (monthly_savings * 12 * annual_interest_rate)

print(f"Your monthly savings are {monthly_savings}.")

print(f"Projected savings after one year, with interest, is: {Projected_Savings}")