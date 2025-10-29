import json
import os

USER_FILE = os.path.join("Database", "users.json")

class UserModel:
    def load_users(self):
        try:
            if not os.path.exists(USER_FILE):
                return []
            with open(USER_FILE, "r") as file:
                return json.load(file)
        except Exception:
            return []

    def save_users(self, users):
        with open(USER_FILE, "w") as file:
            json.dump(users, file, indent=2)
