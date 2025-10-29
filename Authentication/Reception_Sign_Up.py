import json
import os
import getpass

USERS_FILE = os.path.join("Database", "users.json")

class ReceptionSignUp:
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

    def _save_users(self, users):
        with open(USERS_FILE, "w") as file:
            json.dump(users, file, indent=2)

    def sign_up(self):
        print("\n===== RECEPTIONIST SIGN UP =====")
        while True:
            name = input("Enter Your Name: ").strip()
            if not name:
                print("Please enter your name.")
                continue
            break

        while True:
            email = input("Enter Your Email: ").strip()
            if not email:
                print("Please enter your email.")
                continue
            if "@" not in email or "." not in email:
                print("Please enter a valid email address (example@example.com).")
                continue
            break

        while True:
            password = getpass.getpass("Enter Your Password (min 6 chars): ").strip()
            if len(password) < 6:
                print("Password must be at least 6 characters.")
                continue
            password2 = getpass.getpass("Confirm Password: ").strip()
            if password != password2:
                print("Passwords do not match. Try again.")
                continue
            break

        users = self._load_users()
        for u in users:
            if u.get("email") == email:
                print("This email is already registered. Please login instead.")
                return None

        new_user = {"name": name, "email": email, "password": password, "role": "reception"}
        users.append(new_user)
        self._save_users(users)
        print(f"\nReceptionist '{name}' registered successfully!\n")
        return new_user
