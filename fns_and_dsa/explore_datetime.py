from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_date)
    return current_date

def calculate_future_date():
    days = int(input("Enter the number of days to add to the current date:"))
    current_date = display_current_datetime()
    future_date = current_date + timedelta(days=days)
    formatted_future = future_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Future Date and Time:", formatted_future)
    return formatted_future

calculate_future_date()
