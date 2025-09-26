from datetime import date, datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date
    print(current_date)

def calculate_future_date():
    user = int(input("Enter number of days into the future: "))
    future_date = display_current_datetime() + timedelta(days = user)
    return future_date

print(calculate_future_date())
       