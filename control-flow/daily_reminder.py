task = input("Enter your task: ")
priority = input("priority (high, medium, low): ")
time_bound = input("Is this task time-bound? (yes/no): ")

match priority:
    case "high":
        print(f"Reminder: {task} is a {priority} priority task")
    case "medium":
        print(f"Reminder: {task} is a {priority} priority task")
    case "low":
        print(f"Reminder: {task} is a {priority} priority task")
    
if time_bound == "yes":
    print("that requires immediate attention today")
else:
    print("Consider completing it when you have free time.")