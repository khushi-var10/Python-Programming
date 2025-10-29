import json
import os
import getpass

USERS_FILE = os.path.join("Database", "users.json")

class ReceptionSignIn:
    def __init__(self):
        pass

    def _load_users(self):
        try:
            if not os.path.exists(USERS_FILE):
                return []
            with open(USERS_FILE, "r") as file:
                return json.load(file)
        except Exception:
            return []

    def sign_in(self):
        print("\n===== RECEPTIONIST LOGIN =====")
        users = self._load_users()
        if not users:
            print("No receptionists found. Please sign up first.\n")
            return None

        while True:
            email = input("Enter Your Email: ").strip()
            if not email:
                print("Please enter your email\n")
                continue
            password = getpass.getpass("Enter Your Password: ").strip()
            if not password:
                print("Please enter your password.\n")
                continue

            for u in users:
                if u.get("email") == email and u.get("password") == password:
                    print(f"\nWelcome back, {u.get('name')}!\n")
                    return u
            print("Invalid email or password. Try again.\n")
