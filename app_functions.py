import csv

# List to store all job applications
applications = []


# -----------------------------------------
# Add New Application
# -----------------------------------------
def add_application():

    print("\n----- Add New Job Application -----")

    company = input("Enter Company Name: ")
    role = input("Enter Job Role: ")
    location = input("Enter Location: ")
    package = input("Enter Expected Package (LPA): ")
    status = input("Enter Status: ")

    application = {
        "company": company,
        "role": role,
        "location": location,
        "status": status,
        "package": package
    }

    applications.append(application)

    print("\nApplication Added Successfully!")

    print("\nApplication Details")
    print("--------------------------")
    print(f"Company : {application['company']}")
    print(f"Role    : {application['role']}")
    print(f"Location: {application['location']}")
    print(f"Status  : {application['status']}")
    print(f"Package : {application['package']} LPA")

    print(f"\nTotal Applications Stored: {len(applications)}")


# -----------------------------------------
# View Applications
# -----------------------------------------
def view_applications():

    print("\n========== ALL APPLICATIONS ==========")

    if len(applications) == 0:
        print("No applications found.")
        return

    for application in applications:

        print("----------------------------")
        print(f"Company : {application['company']}")
        print(f"Role    : {application['role']}")
        print(f"Location: {application['location']}")
        print(f"Status  : {application['status']}")
        print(f"Package : {application['package']} LPA")

    print("----------------------------")
    print(f"Total Applications: {len(applications)}")


# -----------------------------------------
# Search Application
# -----------------------------------------
def search_application():

    company_name = input("\nEnter Company Name to Search: ")

    found = False

    for application in applications:

        if application["company"].lower() == company_name.lower():

            print("\nApplication Found!")
            print("----------------------------")
            print(f"Company : {application['company']}")
            print(f"Role    : {application['role']}")
            print(f"Location: {application['location']}")
            print(f"Status  : {application['status']}")
            print(f"Package : {application['package']} LPA")

            found = True
            break

    if not found:
        print("\nNo application found for this company.")


# -----------------------------------------
# Update Application
# -----------------------------------------
def update_application():

    company_name = input("\nEnter Company Name to Update: ")

    found = False

    for application in applications:

        if application["company"].lower() == company_name.lower():

            print("\nCurrent Status:", application["status"])

            new_status = input("Enter New Status: ")

            application["status"] = new_status

            print("\nStatus Updated Successfully!")

            found = True
            break

    if not found:
        print("\nApplication not found.")


# -----------------------------------------
# Delete Application
# -----------------------------------------
def delete_application():

    company_name = input("\nEnter Company Name to Delete: ")

    found = False

    for application in applications:

        if application["company"].lower() == company_name.lower():

            print("\nApplication Found!")
            print("----------------------------")
            print(f"Company : {application['company']}")
            print(f"Role    : {application['role']}")
            print(f"Location: {application['location']}")
            print(f"Status  : {application['status']}")
            print(f"Package : {application['package']} LPA")

            confirm = input("\nAre you sure you want to delete this application? (yes/no): ")

            if confirm.lower() == "yes":
                applications.remove(application)
                print("\nApplication Deleted Successfully!")
            else:
                print("\nDeletion Cancelled.")

            found = True
            break

    if not found:
        print("\nApplication not found.")


# -----------------------------------------
# Save to CSV
# -----------------------------------------
def save_to_csv():

    with open("data.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Company", "Role", "Location", "Status", "Package"])

        for application in applications:

            writer.writerow([
                application["company"],
                application["role"],
                application["location"],
                application["status"],
                application["package"]
            ])

    print("\nApplications Saved Successfully!")


# -----------------------------------------
# Load from CSV
# -----------------------------------------
def load_from_csv():

    try:

        with open("data.csv", "r") as file:

            reader = csv.DictReader(file)

            applications.clear()

            for row in reader:

                applications.append({
                    "company": row["Company"],
                    "role": row["Role"],
                    "location": row["Location"],
                    "status": row["Status"],
                    "package": row["Package"]
                })

        print(f"\n{len(applications)} application(s) loaded successfully.")

    except FileNotFoundError:
        print("\nNo previous data found.")