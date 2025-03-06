import ForgotPassword as FP
from CreateProject import create_project as CP
import ViewFiles as VF
import EditProject as EP
import DeleteProject as DP
import SearchProject as SP
#User Main Menu
def UserMenu(user):
    print(f"Welcome, {user['First Name']} {user['Last Name']}!")

    while True:
        print("\nMain Menu:")
        print("1. Project Management")
        print("2. Change Password")
        print("3. Logout")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                manage_projects(user)
            elif choice == 2:
                FP.change_password()
            elif choice == 3:
                print("Logging out.")
                break
            elif choice == 0:
                print("Exiting the program.")
                exit(0)
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid choice.")

#Projects Main Menu
def manage_projects(user):
    while True:
        print("\nProject Management:")
        print("1. Create Project")
        print("2. View Projects")
        print("3. Edit Projects")
        print("4. Delete Project")
        print("5. Search for a Project using Date")
        print("0. Back to Main Menu")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                CP(user)
            elif choice == 2:
                VF.view_data('Projects_Data.json')
            elif choice == 3:
                EP.edit_projects(user)
            elif choice == 4:
                DP.delete_project(user)
            elif choice == 5:
                pass
                SP.search_project()
            elif choice == 0:
                print("Returning to the Main Menu.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")
        except ValueError:
            print("Invalid input. Please enter a valid choice.")