# Main Program

from timetable import add_timetable, view_timetable
from tasks import add_task, view_tasks
from trackingg import update_task
from reports import view_report
from Validation import get_valid_choice


timetable = [ ]
tasks = [ ]


while True:
    print("\n==============================================")
    print("       COLLEGE TIMETABLE & TASK PLANNER")
    print("==============================================")

    print("1. Add Timetable")
    print("2. View Timetable")
    print("3. Add Academic Task")
    print("4. View Academic Tasks")
    print("5. Update Task Status")
    print("6. View Academic Report")
    print("7. Exit")

    choice = get_valid_choice("Select your choice: ", 1, 7)

    # Module 1: Timetable Management

    if choice == 1:

        add_timetable(timetable)


    elif choice == 2:

        view_timetable(timetable)


    # Module 2: Task Management

    elif choice == 3:

        add_task(tasks)


    elif choice == 4:

        view_tasks(tasks)


    # Module 3: Task Tracking

    elif choice == 5:

        update_task(tasks)


    # Module 4: Reports

    elif choice == 6:

        view_report(timetable, tasks)


    # Exit

    elif choice == 7:

        print("\nThank you for using College Timetable & Task Planner!")
        break