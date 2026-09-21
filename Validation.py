# Module 5: Validation Module

def get_valid_choice(message, minimum, maximum):

    while True:

        choice = input(message)

        if choice.isdigit():

            choice = int(choice)

            if choice >= minimum and choice <= maximum:
                return choice

        print("Invalid choice! Please try again.")