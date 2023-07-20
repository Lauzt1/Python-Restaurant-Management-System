import random
import datetime
from tabulate import tabulate

def displayMenu():
    with open('menu.txt', 'r') as f:
        for line in f:
            print(line)

def displayReservation():
    # Table headers
    headers = ["Date", "Slot", "Name", "Email", "ID", "Order"]
    # Format string for table row
    row_format = "{:<12} {:<8} {:<15} {:<25} {:<10} {:<5}"

    # Print table headers
    print(row_format.format(*headers))
    print("-" * 100)

    # Open the file and read reservations
    with open('reservation.txt', 'r') as file:
        reservations = file.readlines()

    # Print each reservation
    for reservation in reservations:
        # Remove leading/trailing whitespaces and split the fields
        fields = reservation.strip().split('|')
        # Print formatted row
        print(row_format.format(*fields))

def mealRecommendation():
    with open('menu.txt', 'r') as f:
        menu = f.read().splitlines()
    recommendations = random.sample(menu, min(len(menu), 3))
    print("Chef's recommendations:")
    for recommendation in recommendations:
        print(recommendation)

def addReservation():
    while True:
        try:
            month = int(input("Enter the month (1-12): "))
            day = int(input("Enter the day (1-31): "))
            input_date = datetime.datetime(datetime.datetime.now().year, month, day).date()
            today = datetime.datetime.now().date()
            if input_date >= today + datetime.timedelta(days=5):
                date = input_date.strftime("%Y-%m-%d")
            else:
                print("Error: Please enter a date that is more than 5 days from today.")
                continue
        except ValueError:
            print("Invalid input. Please enter valid month and day.")
            continue

        try:
            slot = int(input("Please select a time slot:\n1. 12:00 pm - 02:00 pm\n2. 02:00 pm - 04:00 pm\n3. 06:00 pm - 08:00 pm\n4. 08:00 pm - 10:00 pm\nEnter your choice (1-4): "))
            if 1 <= slot <= 4:
                slot_times = ["12:00 pm - 02:00 pm", "02:00 pm - 04:00 pm", "06:00 pm - 08:00 pm", "08:00 pm - 10:00 pm"]
                slot1 = slot_times[slot - 1]
            else:
                print("Invalid selection. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone number: ")

        try:
            pax = int(input("Enter the pax number: "))
            if pax >= 5:
                print("Maximum 4 pax allowed")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        with open('reservation.txt', 'r') as file:
            reservations = file.readlines()

        matching_reservations = [r for r in reservations if r.startswith(date + '|' + slot1)]

        if len(matching_reservations) < 8:
            number = len(matching_reservations) + 1
            reservation = f"{date}|{slot1}|{name}|{email}|{phone}|{pax}|{number}\n"
            with open('reservation.txt', 'a') as file:
                file.write(reservation)
            print("Reservation added successfully!\n")
        else:
            print("Error: This date and time slot is full. Maximum of 8 reservations allowed.\n")
        break

def main():
    while True:
        print("----------------------------------------------------------------------\n\n=============================\n=        Main Menu          =\n=============================")
        print("0. Quit\n1. Display Reservations\n2. Display Menu\n3. Add Reservation\n4. Delete Reservation\n5. Generate Recommendations")
        try:
            selection = int(input("Your Selection: "))
            if selection == 0:
                break
            elif selection == 1:
                displayReservation()
            elif selection == 2:
                displayMenu()
            elif selection == 3:
                addReservation()
            elif selection == 5:
                mealRecommendation()
            else:
                print("Invalid selection!")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue


if __name__ == "__main__":
    main()
