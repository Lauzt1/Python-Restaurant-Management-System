import datetime
import random


def displayMenu():
    #Print's menu list for user to see 
    with open('menu_19115062.txt', 'r') as f: 
        for line in f:
            print(line)

def mealRecommendation():
    menu = open('menu_19115062.txt').read().splitlines()
    print("Chef's recommendations:")
#Generates 3 random recommendations from menu list
    for i in range(3):
        print(random.choice(menu))

def displayReservation():
    # Table headers
    headers = ["Date", "Slot", "Name", "Email", "Phone", "Pax", "Group Number", "Reservation ID"]
    # Format string for table row
    row_format = "{:<12} {:<22} {:<12} {:<25} {:<15} {:<5} {:<13} {:<10}"

    # Print table headers
    print(row_format.format(*headers))
    print("-" * 125)

    # Open the file and read reservations
    with open('reservation_19115062.txt', 'r') as file:
        reservations = file.readlines()

    # Print each reservation
    for reservation in reservations:
        # Remove leading/trailing whitespaces and split the fields
        fields = reservation.strip().split('|')
        # Print formatted row
        print(row_format.format(*fields))

def randomID(length=8):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    #Generates unique 8 character ID for each reservation
    return ''.join(random.choice(characters) for i in range(8))

def addReservation():
    # Prompt the user for reservation information
    while True:
        # Enter month and day, year will default on this year
        try:
            month = int(input("Enter the month (1-12): "))
            day = int(input("Enter the day (1-31): "))
            input_date = datetime.datetime(datetime.datetime.now().year, month, day).date()
            today = datetime.datetime.now().date()
            if input_date >= today + datetime.timedelta(days=5):
                date = input_date.strftime("%Y-%m-%d")
            else:
                print("Error: Please enter a date that is more than 5 days from today.")
                break
        except ValueError:
            print("Invalid input. Please enter valid month and day.")
            break

        # Select time slot by entering number
        try:
            slot = int(input("Please select a time slot:\n1. 12:00 pm - 02:00 pm\n2. 02:00 pm - 04:00 pm\n3. 06:00 pm - 08:00 pm\n4. 08:00 pm - 10:00 pm\nEnter your choice (1-4): "))
            if 1 <= slot <= 4:
                if slot == 1:
                    slot1 = "12:00 pm - 02:00 pm"
                elif slot == 2:
                    slot1 = "02:00 pm - 04:00 pm"
                elif slot == 3:
                    slot1 = "06:00 pm - 08:00 pm"
                elif slot == 4:
                    slot1 = "08:00 pm - 10:00 pm"
            else:
                print("Invalid selection. Please try again.")
                break
        except ValueError:
                print("Invalid input. Please enter a number.")
                break
        
        # Name input
        name = input("Enter name: ")
        if name.strip() and len(name) <= 20:
            pass
        else:
            print("Invalid name.")
            break

        # Email input and check
        email = input("Enter email: ")
        if "@" in email and ".com" in email:
            pass
        else:
            print("Error: Invalid email format.")
            break

        #Phone input and check
        phone = input("Enter phone number: ")
        if phone.startswith("01") and not len(phone) != 10:
            pass
        else:
            print("Error: Invalid phone number format.")
            break

        
        # Generate a random ID for the reservation
        reservationID = randomID()

        # Enter pax number
        try:
            pax = input("Enter the pax number: ")
            if int(pax) >= 5:
                print("Maximum 4 pax allowed")
                break
        except ValueError:
                print("Invalid input. Please enter a number.")
                break

        # Check if slot is full and write if no exception
        with open('reservation_19115062.txt', 'r') as file:
            reservations = file.readlines()

        matching_reservations = [r for r in reservations if r.startswith(date + '|' + slot1)]

        if len(matching_reservations) < 8:
            number = len(matching_reservations) + 1
            reservation = f"{date}|{slot1}|{name}|{email}|{phone}|{pax}|{number}|{reservationID}\n"
            with open('reservation_19115062.txt', 'a') as file:
                file.write(reservation)
            print("Reservation added successfully!")
            print(f"Reservation ID: {reservationID}\n")
        else:
            print("Error: This date and time slot is full. Maximum of 8 reservations allowed.\n")
        break
    
    # Prompt user for another reservation
    try:
        another = input("Would you like to make another reservation? (y/n)")
        if another == "y":
            addReservation()
        elif another == "n":
            pass
    except ValueError:
        print("Invalid input. Please enter y or n.")

def deleteReservation():
    #Ask user to enter the ID of their reservation that they want to delete
    idDelete = input("Enter the ID of the reservation you want to delete: ")
    
    with open('reservation_19115062.txt', 'r') as file:
        lines = file.readlines()

    currentReservations = [line for line in lines if line.split('|')[-1].strip() == idDelete]
    #If Reservation exists
    if len(currentReservations) > 0:
        print("Is this your reservation?:")
        #Displays reservation to user so they can confirm it is thiers 
        for reservation in currentReservations:
            print(reservation.strip())
        #Asks user to confirm thier deletion of thier reservation
        confirm = input("Are you sure you want to delete this reservation? (y/n): ")
        if confirm == 'y':
            #Rewrites reservations into the list except for the one that has been deleted
            with open('reservation_19115062.txt', 'w') as file:
                for line in lines:
                    if line not in currentReservations:
                        file.write(line)
            print("The reservation has been deleted.\n")
        else:
            print("Deletion canceled.\n")
    else:
        print("No reservations found with the given ID.\n")

    try:
        #Prompts user if they would like to delete another reservation
        another = input("Would you like to delete more reservations? (y/n): ")
        if another == "y":
            deleteReservation()
        elif another == "n":
            pass #If the user does not want to delete any more reservations the function is exited 
    except ValueError:
        #Checks for valid input from the user
        print("Invalid input. Please enter y or n.")


def editReservation():
    print("==== Update/Edit Reservation ====")
    reservation_id_to_edit = input("Enter the ID of the reservation to update: ")

    # Mapping slot number to time slot
    slot_mapping = {
        '1': "12:00 pm - 02:00 pm",
        '2': "02:00 pm - 04:00 pm",
        '3': "06:00 pm - 08:00 pm",
        '4': "08:00 pm - 10:00 pm"
    }

    # Read existing reservations from the file
    with open('reservation_19115062.txt', 'r') as file:
        reservations = file.readlines()

    updated = False

    with open('reservation_19115062.txt', 'r+') as file:
        for reservation in reservations:
            fields = reservation.strip().split('|')
            if fields[-1] == reservation_id_to_edit:
                updated = True
                print(f"Current reservation: {reservation}")
                
                while True:
                    new_month = input("Enter the new month (MM): ")
                    new_day = input("Enter the new day (DD): ")
                    try:
                        new_date = datetime.datetime.strptime(f"2023-{new_month}-{new_day}", "%Y-%m-%d")
                        formatted_date = new_date.strftime("%Y-%m-%d")
                        break
                    except ValueError:
                        print("Invalid date format. Please enter a valid date.")
                    
                new_session = input("Enter the new session (1, 2, 3, or 4) [Leave blank to keep the current value]: ")
                if new_session:
                    if new_session not in ['1', '2', '3', '4']:
                        print("Invalid slot. Please enter a valid slot number.")
                        file.write(reservation)  # Add the current reservation back to the file
                        continue  # Skip updating and move to the next reservation
                else:
                    new_session = fields[1]  # Keep the current value

                new_pax = input("Enter the new number of people [Leave blank to keep the current value]: ")
                if new_pax:
                    if int(new_pax) > 4:
                        print("Error: Number of people cannot exceed 4. The reservation will not be updated.")
                        file.write(reservation)  # Add the current reservation back to the file
                        continue  # Skip updating and move to the next reservation
                
                new_phone = input("Enter the new phone number [Leave blank to keep the current value]: ")
                if new_phone and (not new_phone.startswith("01") or len(new_phone) != 10):
                    print("Error: Invalid phone number format. The reservation will not be updated.")
                    file.write(reservation)  # Add the current reservation back to the file
                    continue  # Skip updating and move to the next reservation
                elif not new_phone:  # If the user left the phone number blank
                    new_phone = fields[4]  # Keep the current value
                
                new_email = input("Enter the new email [Leave blank to keep the current value]: ")
                if new_email:
                    if "@" not in new_email or ".com" not in new_email:
                        print("Error: Invalid email format. The reservation will not be updated.")
                        file.write(reservation)  # Add the current reservation back to the file
                        continue  # Skip updating and move to the next reservation
                
                new_slot = slot_mapping.get(new_session)
                if not new_slot:
                    new_slot = fields[1]

                # Create a new list of reservations excluding the one being edited
                updated_reservations = [r for r in reservations if r.strip().split('|')[-1] != reservation_id_to_edit]

                # Check if the number of reservations on the new slot is less than 8
                if new_slot:
                    count_reservations_on_new_slot = sum(1 for r in updated_reservations if r.strip().split('|')[1] == new_slot)
                    if count_reservations_on_new_slot > 8:
                        print(f"Error: The slot {new_slot} is fully booked. The reservation will not be updated.")
                        file.write(reservation)  # Add the current reservation back to the file
                        continue  # Skip updating and move to the next reservation
                        
                fields[0] = formatted_date
                fields[1] = new_slot 
                fields[4] = new_phone
                fields[3] = new_email or fields[3]
                fields[5] = new_pax or fields[5]

                updated_reservation = '|'.join(fields)
                print(f"Updated reservation: {updated_reservation}")
                file.write(updated_reservation + "\n")
            else:
                file.write(reservation)

    if not updated:
        print("No reservations found with the given ID.")

    another_edit = input("Would you like to edit another reservation? (y/n): ").lower()
    if another_edit == "y":
        editReservation()
    else:
        print("Reservation editing completed.")

def main():
    while True:
        print(("-" * 120) +"\n\n=============================\n=        Main Menu          =\n=============================")
        print("0. Quit\n1. Display Reservations\n2. Display Menu\n3. Chef's Recommendation\n4. Add Reserveation\n5. Delete Reservation\n6. Edit Reservation")
        selection = (input("Your Selection: "))
        match selection:
            case '0':
                break
            case '1':
                displayReservation()
            case '2':
                displayMenu()
            case '3':
                mealRecommendation()
            case '4':
                addReservation()
            case '5':
                deleteReservation()
            case '6':
                editReservation()
            case default:
                print("Invalid selection!")

if __name__ == "__main__":
    main()
