import getpass

class AdminSignIn:
    def __init__(self):
        self.__name = "Khushi Varshney"
        self.__email = "khushi@gmail.com"
        self.__password = "khushi123123"

    def admin_login(self):
        print("\n===== ADMIN LOGIN =====")
        while True:
            email = input("Enter Admin Email: ").strip()
            if not email:
                print("Please enter your email.\n")
                continue

            password = getpass.getpass("Enter Admin Password: ").strip()
            if not password:
                print("Please enter your password.\n")
                continue

            if email == self.__email and password == self.__password:
                print(f"\nWelcome, {self.__name}! You are logged in as Admin.\n")
                return True
            else:
                print("\nInvalid email or password. Please try again.\n")