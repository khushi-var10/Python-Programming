import json
import os

MENU_FILE = os.path.join("Database", "menu.json")

class MenuModel:
    def load_menu(self):
        try:
            if not os.path.exists(MENU_FILE):
                return {"Morning": [], "Lunch": [], "Dinner": []}
            with open(MENU_FILE, "r") as file:
                data = json.load(file)
                for k in ("Morning", "Lunch", "Dinner"):
                    if k not in data:
                        data[k] = []
                return data
        except Exception:
            return {"Morning": [], "Lunch": [], "Dinner": []}

    def save_menu(self, data):
        with open(MENU_FILE, "w") as file:
            json.dump(data, file, indent=2)

    def next_id(self):
        data = self.load_menu()
        all_ids = [item["id"] for cat in data.values() for item in cat]
        return max(all_ids, default=0) + 1
