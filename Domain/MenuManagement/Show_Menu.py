from Model.Menu_Model import MenuModel

class ShowMenu:
    def display_menu(self):
        menu = MenuModel().load_menu()
        print("\n============================")
        print("   🌱  Satvik Zaika  🌱")
        print("        MENU CARD")
        print("============================")
        for time_name in ("Morning", "Lunch", "Dinner"):
            items = menu.get(time_name, [])
            print(f"\n----- {time_name.upper()} MENU -----")
            print("S.No | Dish Name                     | Half Price | Full Price")
            print("----------------------------------------------------------------")
            if not items:
                print("  (No items in this section)")
            else:
                for item in items:
                    id_str = str(item.get("id", ""))
                    name = item.get("name", "")
                    half = item.get("half_price", "")
                    full = item.get("full_price", "")
                    print(f"{id_str:>4} | {name:<28} | Rs.{half:<9} | Rs.{full}")
        print()
