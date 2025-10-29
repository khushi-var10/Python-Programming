from Model.Menu_Model import MenuModel

class AddItem:
    def add_new_item(self):
        menumodel = MenuModel()
        menu = menumodel.load_menu()
        print("\nWhich menu do you want to add item in?")
        print("1. Morning\n")
        print("2. Lunch\n")
        print("3. Dinner")
        while True:
            choice = input("Enter your choice (1-3): ").strip()
            if choice not in ("1", "2", "3"):
                print("Please enter 1, 2 or 3.")
                continue
            key = {"1": "Morning", "2": "Lunch", "3": "Dinner"}[choice]
            break

        while True:
            name = input("Enter dish name: ").strip()
            if not name:
                print("Please enter dish name.")
                continue
            break

        while True:
            half_in = input("Enter half price: ").strip()
            try:
                half = float(half_in)
                if half <= 0:
                    print("Price must be positive.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number for half price.")

        while True:
            full_in = input("Enter full price: ").strip()
            try:
                full = float(full_in)
                if full <= 0:
                    print("Price must be positive.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number for full price.")

        new_id = menumodel.next_id()
        menu[key].append({"id": new_id, "name": name, "half_price": half, "full_price": full})
        menumodel.save_menu(menu)
        print(f"Item '{name}' added to {key} with ID {new_id}.\n")