import random
import datetime

# divider = "----------------------------------------------------------------------"

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
    menu = open('menu.txt').read().splitlines()
    print("Chef's recommendation: "+random.choice(menu))
    #try to make it print more than 1 recommendation (generate from list? do later)

def addReservation():
    # Prompt the user for reservation information
    date = input("Enter the date (YYYY-MM-DD): ")
    slot = input("Enter the slot: ") #()
    name = input("Enter the name: ")
    email = input("Enter the email: ")
    ID = input("Enter the ID: ")
    pax = input("Enter the pax number: ")

    # Format the reservation information
    reservation = f"{date}|Slot{slot}|{name}|{email}|{ID}|{pax}\n"

    # Write the reservation to the file
    with open('reservation.txt', 'a') as file:
        file.write(reservation)
    print("Reservation added successfully.")

def main():
    while True:
        print("----------------------------------------------------------------------\n\n=============================\n=        Main Menu          =\n=============================")
        print("0. Quit\n1. Display Reservations\n2. Display Menu\n3. Add Reserveation\n4. Delete Reservation\n5. Generate Recommendations")
        selection = int(input("Your Selection: "))
        match selection:
            case 0:
                break
            case 1:
                displayReservation()
            case 2:
                displayMenu()
            # case 3:
            #     addReservation()
            # case 4:
            #     delReservation()
            case 5:
                mealRecommendation()
            case default:
                print("Invalid selection!")


if __name__ == "__main__":
    main()

