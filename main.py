from Authentication.Admin_Sign_In import AdminSignIn
from Authentication.Reception_Sign_Up import ReceptionSignUp
from Authentication.Reception_Sign_In import ReceptionSignIn

from Domain.MenuManagement.Show_Menu import ShowMenu
from Domain.MenuManagement.Add_Item import AddItem
from Domain.MenuManagement.Update_Item import UpdateItem
from Domain.MenuManagement.Delete_Item import DeleteItem

from Domain.OrderManagement.Take_Order import TakeOrder
from Domain.OrderManagement.Generate_Bill import GenerateBill

from Report.Order_Report import OrderReport
from Report.Revenue_Report import RevenueReport


def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. Show Menu")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Orders Report")
        print("6. Revenue Report")
        print("7. Logout")

        choice = input("Enter choice (1-7): ").strip()

        if choice == "1": ShowMenu().display_menu()
        elif choice == "2": AddItem().add_new_item()
        elif choice == "3": UpdateItem().update_item()
        elif choice == "4": DeleteItem().delete_item()
        elif choice == "5": OrderReport().show_all_orders()
        elif choice == "6": RevenueReport().show_revenue()
        elif choice == "7": break
        else: print("Invalid input.")


def reception_menu(user):
    while True:
        print(f"\n--- RECEPTION ({user.get('name')}) ---")
        print("1. Show Menu")
        print("2. Take Order")
        print("3. Logout")

        choice = input("Enter choice (1-3): ").strip()

        if choice == "1": ShowMenu().display_menu()
        elif choice == "2":
            order = TakeOrder().take_order(user.get("name"))
            if order: GenerateBill().print_bill(order)
        elif choice == "3": break
        else: print("Invalid input.")


def main():
    while True:
        print("\n--- SATVIK ZAIKA SYSTEM ---")
        print("1. Admin Login")
        print("2. Reception Sign Up")
        print("3. Reception Login")
        print("4. Exit")

        choice = input("Enter choice (1-4): ").strip()

        if choice == "1":
            if AdminSignIn().admin_login():
                admin_menu()

        elif choice == "2":
            ReceptionSignUp().sign_up()

        elif choice == "3":
            user = ReceptionSignIn().sign_in()
            if user:
                reception_menu(user)

        elif choice == "4":
            print("Exiting System...")
            break

        else:
            print("Wrong input.")


if __name__ == "__main__":
    main()
