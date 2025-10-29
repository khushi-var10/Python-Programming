from Model.Menu_Model import MenuModel

class UpdateItem:
    def update_item(self):
        menumodel = MenuModel()
        menu = menumodel.load_menu()
        print("\nCurrent items (ID - Name):")
        for cat, items in menu.items():
            for it in items:
                print(f"{it['id']}: {it['name']} ({cat})")
        while True:
            id_in = input("Enter item ID to update: ").strip()
            if not id_in.isdigit():
                print("Please enter a valid numeric ID.")
                continue
            item_id = int(id_in)
            break

        found = None
        found_cat = None
        for cat, items in menu.items():
            for it in items:
                if it.get("id") == item_id:
                    found = it
                    found_cat = cat
                    break
            if found:
                break

        if not found:
            print("Item ID not found.")
            return

        print(f"Current: {found.get('name')} | Half Rs.{found.get('half_price')} | Full Rs.{found.get('full_price')}")
        new_name = input("New name (leave blank to keep): ").strip()
        if new_name:
            found["name"] = new_name

        while True:
            new_half = input("New half price (blank to keep): ").strip()
            if not new_half:
                break
            try:
                newhalf = float(new_half)
                if newhalf <= 0:
                    print("Price must be positive.")
                    continue
                found["half_price"] = newhalf
                break
            except ValueError:
                print("Enter a valid number.")

        while True:
            new_full = input("New full price (blank to keep): ").strip()
            if not new_full:
                break
            try:
                newfull = float(new_full)
                if newfull <= 0:
                    print("Price must be positive.")
                    continue
                found["full_price"] = newfull
                break
            except ValueError:
                print("Enter a valid number.")

        menumodel.save_menu(menu)
        print(f"Item ID {item_id} updated successfully in {found_cat}.\n")
