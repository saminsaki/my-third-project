task_names = []
task_statuses = []
task_durations = []
for i in range(200):

    command = input("\n Enter command ( for commands enter help):").lower()

    if command == 'help':

        print("""
        Commands:
            add: Add a New Task
            display: Display all tasks
            remove: Remove a task by Name
            edit: Edit the name of an existing task
            search: Search for a task by name
            mark: Mark a task as done and record duration
            details: Show details of all tasks
            help: Show this help message
            exit: Exit the program
        """)
    elif command == 'add':
        task_name = input("Enter task name")
        if task_name in task_names:
            print("Task already exist")
        else:
            task_names.append(task_name)
            task_statuses.append(False)
            task_durations.append(None)
            print(f"Task '{task_name} added successfully.")

    elif command == 'display':
        if len(task_names) == 0 :
            print("Empty !")
        for name, status, duration in zip(task_names, task_statuses, task_durations):
            status_task = "Not Done"
            if status:
                status_task = "Done"
            print(f"Task: {name}, Status: {status_task}, Duration : {duration}")
    elif command == "remove":
        task_name = input("Enter task name to remove:")
        if task_name in task_names:
            index = task_names.index(task_name)
            task_names.pop(index)
            task_statuses.pop(index)
            task_durations.pop(index)
            print(f"Task {task_name} Removed successfully.")
        else:
            print("Task not found")

    elif command == 'edit':

        old_name = input("Enter the current task name:")
        new_name = input("Enter the new task name: ")

        if old_name in task_names:
            if new_name in task_names:
                print(f"Task with the name {new_name} already exist")
            else:
                index = task_names.index(old_name)
                task_names[index] = new_name
                print(f"Task {old_name} has been renamed to {new_name}")
        else:
            print("Task Not Found!")

    elif command == "search":
        task_name = input("Enter yask name to search: ")
        if task_name in task_names:
            index = task_names.index(task_name)
            status = task_statuses[index]
            duration = task_durations[index]
            status_task = "Not Done"
            if status:
                status_task = "Done"
            print(f"Task {task_name}, Status: {status_task}, Duration: {duration}")
        else:
            print("Task Not found!")
        
    elif command == 'mark':
        task_name = input("Enter Task name to mark as done")
        if task_name in task_names:
            index = task_names.index(task_name)
            if task_statuses[index]:
                print("Task is already marked as done")
            else:
                start_time = input("Enter the start time in the format HH:MM  :")
                end_time = input("Enter the end time in the format HH:MM :")
                start_time_parts = start_time.split(':')
                end_time_parts = end_time.split(':')

                start_hours = int(start_time_parts[0])
                start_minute = int(start_time_parts[1])

                end_hours = int(end_time_parts[0])
                end_minute = int(end_time_parts[1])

                duration_minutes = (end_hours*60 + end_minute) - (start_hours*60 + start_minute)
                duration_hours = duration_minutes // 60
                duration_minutes %= 60

                duration_str = f"{duration_hours:02d}:{duration_minutes:02d}"
                # 01:30 ----> hours : 1 , minutes : 30
                task_statuses[index] = True
                task_durations[index] = duration_str

                print(f"Task '{task_name}' marked as done. Duration: {duration_str}")
        else:
            print("Task Not Found!")
    
    elif command == 'details':
        total_tasks = len(task_names)
        total_minutes = 0

        for duration in task_durations:
            if duration:
                hours, minutes = duration.split(':')
                total_minutes += int(hours) * 60 + int(minutes)
        hours_worked = total_minutes / 60
        completed_tasks = sum(task_statuses)
        uncompleted_tasks = total_tasks - completed_tasks

        print(f"Total tasks: {total_tasks}")
        print(f"Hours worked : {hours_worked}")
        print(f"completed_tasks: {completed_tasks}")
        print(f"uncompleted_tasks: {uncompleted_tasks}")

    elif command == 'exit':
        break
    elif command == "":
        continue

    else:
        print("Unknown Command!")