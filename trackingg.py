# Module 3: Task Tracking

def update_task(tasks):

    print("\n========== Update Task ==========")

    if len(tasks) == 0:
        print("No tasks available to update.")
        return

    for i in range(len(tasks)):

        print(i + 1, ".", tasks[i]["task_name"])

    choice = input("\nSelect task number: ")

    if choice.isdigit():

        task_number = int(choice)

        if task_number >= 1 and task_number <= len(tasks):

            print("\nSelected Task:", tasks[task_number - 1]["task_name"])

            print("1. Pending")
            print("2. Completed")

            status_choice = input("Select status: ")

            if status_choice == "1":
                tasks[task_number - 1]["status"] = "Pending"
                print("\nTask status updated to Pending.")

            elif status_choice == "2":
                tasks[task_number - 1]["status"] = "Completed"
                print("\nTask marked as Completed.")

            else:
                print("\nInvalid status choice.")

        else:
            print("\nInvalid task number.")

    else:
        print("\nPlease enter a valid number.")