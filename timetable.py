# Module 1: Timetable Management

def add_timetable(timetable):

    print("\n========== Add Timetable ==========")

    day = input("Enter day: ")
    subject = input("Enter subject: ")
    time = input("Enter class time: ")
    room = input("Enter room number: ")

    entry = {
        "day": day,
        "subject": subject,
        "time": time,
        "room": room
    }

    timetable.append(entry)

    print("\nTimetable added successfully!")


def view_timetable(timetable):

    print("\n========== College Timetable ==========")

    if len(timetable) == 0:
        print("No timetable entries available.")
        return

    for i in range(len(timetable)):

        print("\nTimetable Entry", i + 1)

        print("Day     :", timetable[i]["day"])
        print("Subject :", timetable[i]["subject"])
        print("Time    :", timetable[i]["time"])
        print("Room    :", timetable[i]["room"])