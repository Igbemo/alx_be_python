#This programme helps prioritise task amd a daily reminder using match case
task = input("Enter your task: ")                            #Take the task as a string value
priority = input("Priority (high/medium/low): ")    #priotise th pe task
time = input("Is it time-bound? (yes/no): ")            #holds the time as a boolean value

if time =="yes":
    match priority:
        case "high":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        case "medium":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        case "low":
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today")
            
else:
            print(f"Note: {task} is a {priority} priority task. Consider completing it when you have free time.")
            