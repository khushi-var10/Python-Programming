from Model.Menu_Model import MenuModel

class DeleteItem:
    def delete_item(self):
        menumodel = MenuModel()
        menu = menumodel.load_menu()
        print("\nCurrent items (ID - Name):")
        for cat, items in menu.items():
            for it in items:
                print(f"{it['id']}: {it['name']} ({cat})")

        while True:
            id_in = input("Enter item ID to delete: ").strip()
            if not id_in.isdigit():
                print("Please enter a valid numeric ID.")
                continue
            item_id = int(id_in)
            break

        for cat, items in menu.items():
            for it in items:
                if it.get("id") == item_id:
                    confirm = input(f"Are you sure you want to delete '{it.get('name')}'? (y/n): ").strip().lower()
                    if confirm == "y":
                        items.remove(it)
                        menumodel.save_menu(menu)
                        print("Item deleted successfully.\n")
                        return
                    else:
                        print("Delete cancelled.\n")
                        return
        print("Item ID not found.\n")
