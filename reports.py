# ==========================================
# COLLEGE TIMETABLE & TASK PLANNER
# Module 4: Reports & Summary
# ==========================================

def view_report(timetable, tasks):

    print("\n========== Academic Report ==========")

    print("\nTotal Timetable Entries :", len(timetable))
    print("Total Academic Tasks    :", len(tasks))

    completed = 0
    pending = 0

    for i in range(len(tasks)):

        if tasks[i]["status"] == "Completed":
            completed = completed + 1
        else:
            pending = pending + 1

    print("Completed Tasks         :", completed)
    print("Pending Tasks           :", pending)

    print("\n---------- Task Summary ----------")

    if len(tasks) == 0:
        print("No academic tasks available.")

    else:

        for i in range(len(tasks)):

            print("\nTask", i + 1)
            print("Task Name :", tasks[i]["task_name"])
            print("Subject   :", tasks[i]["subject"])
            print("Deadline  :", tasks[i]["deadline"])
            print("Priority  :", tasks[i]["priority"])
            print("Status    :", tasks[i]["status"])