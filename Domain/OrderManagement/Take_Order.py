from Model.Menu_Model import MenuModel
from Model.Order_Model import OrderModel

class TakeOrder:
    def take_order(self, receptionist_name):
        menumodel = MenuModel()
        ordermodel = OrderModel()
        menu = menumodel.load_menu()
        order_items = []
        print("\nWelcome to Satvik Zaika - Take Order")
        for cat in ("Morning", "Lunch", "Dinner"):
            items = menu.get(cat, [])
            if items:
                print(f"\n--- {cat} ---")
                for it in items:
                    print(f"{it['id']}. {it['name']} (Half Rs.{it['half_price']} / Full Rs.{it['full_price']})")

        while True:
            choice = input("\nEnter item ID to add (or 'done' to finish): ").strip().lower()
            if choice == "done":
                break
            if not choice.isdigit():
                print("Please enter a valid numeric item ID.")
                continue
            item_id = int(choice)
            found = None
            for cat, items in menu.items():
                for it in items:
                    if it.get("id") == item_id:
                        found = it
                        break
                if found:
                    break
            if not found:
                print("Item ID not found. Try again.")
                continue

            while True:
                size = input("Enter size (half/full): ").strip().lower()
                if size not in ("half", "full"):
                    print("Please type 'half' or 'full'.")
                    continue
                break

            while True:
                q_in = input("Enter quantity: ").strip()
                if not q_in.isdigit():
                    print("Please enter a valid integer quantity.")
                    continue
                qty = int(q_in)
                if qty <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                break

            price = found["half_price"] if size == "half" else found["full_price"]
            subtotal = price * qty
            order_items.append({
                "id": found["id"],
                "name": found["name"],
                "size": size,
                "qty": qty,
                "unit_price": price,
                "subtotal": subtotal
            })
            print(f"Added {qty} x {found['name']} ({size}) - Rs.{subtotal}")

        if not order_items:
            print("No items selected. Order cancelled.\n")
            return None

        total = sum(x["subtotal"] for x in order_items)
        tax = round(total * 0.05, 2)
        grand_total = round(total + tax, 2)

        order_data = {
            "receptionist": receptionist_name,
            "items": order_items,
            "total": total,
            "tax": tax,
            "grand_total": grand_total
        }
        saved = ordermodel.add_order(order_data)
        print(f"\nOrder placed. Order ID: {saved.get('id')}  Grand Total: Rs.{grand_total}\n")
        return saved
