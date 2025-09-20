#Task App Reminder App
task = input("Enter your task:")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

if (priority == "high") and (time_bound == "yes"):
    print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
elif (priority == "medium") and (time_bound == "yes"):
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!") 
else:
    print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")   
