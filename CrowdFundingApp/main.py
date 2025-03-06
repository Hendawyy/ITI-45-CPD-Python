import RegisterUser as RU
import UserLogin as UL
import ForgotPassword as FP
import ViewFiles as VF

while True:
    print("\nMenu:")
    print("1. Register")
    print("2. Login")
    print("3. Forgot Password")
    print("4. View Users")
    print("0. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            RU.register_user()
        elif choice == 2:
            UL.login_user()
        elif choice == 3:
            FP.change_password()
        elif choice == 4:
            VF.view_data('Users_Data.json')
        elif choice == 0:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a valid choice.")