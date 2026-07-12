from app_functions import (
    add_application,
    view_applications,
    search_application,
    update_application,
    delete_application,
    save_to_csv,
    load_from_csv
)

# Load saved applications when the program starts
load_from_csv()

while True:

    print("\n====================================")
    print("          CAREERFLOW")
    print("     Job Application Tracker")
    print("====================================")

    print("1. Add Job Application")
    print("2. View Applications")
    print("3. Search Application")
    print("4. Update Application")
    print("5. Delete Application")
    print("6. Save to CSV")
    print("7. Exit")

    try:
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            add_application()

        elif choice == 2:
            view_applications()

        elif choice == 3:
            search_application()

        elif choice == 4:
            update_application()

        elif choice == 5:
            delete_application()

        elif choice == 6:
            save_to_csv()

        elif choice == 7:
            print("\nThank you for using CareerFlow!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 7.")

    except ValueError:
        print("\nPlease enter numbers only.")