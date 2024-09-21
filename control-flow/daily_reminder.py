task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority :
    case "high":
        if time_bound == 'yes':
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        
        else :
            print(f"Reminder: {task} is a high priority task but is not time bound dont underestimate it and complete it now")

    case "medium":
        if time_bound == 'yes':
            print(f"Reminder: {task} is a medium priority task that requires immediate attention today!")
        else :
            print(f"Reminder: {task} is a medium priority task but is not time bound dont underestimate it and complete it now")

    case "low":
        if time_bound == 'yes':
            print(f"Reminder: {task} is a low priority task , Consider completing it on free time")
        
        else :
            print(f"Reminder: {task} is a low priority task , Consider completing it")