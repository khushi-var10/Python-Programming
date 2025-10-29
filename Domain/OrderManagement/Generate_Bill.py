class GenerateBill:
    def print_bill(self, order):
        if not order:
            print("No order to print.\n")
            return
        print("\n==============================")
        print("     🌱 Satvik Zaika BILL 🌱 ")
        print("==============================")
        print(f"Order ID: {order.get('id')}")
        print(f"Date: {order.get('date')}")
        print(f"Taken by: {order.get('receptionist')}")
        print("------------------------------")
        for i, it in enumerate(order.get("items", []), start=1):
            name = it.get("name")
            size = it.get("size")
            qty = it.get("qty")
            unit = it.get("unit_price")
            sub = it.get("subtotal")
            print(f"{i}. {name} ({size}) x{qty} @ Rs.{unit} = Rs.{sub}")
        print("------------------------------")
        print(f"Subtotal: Rs.{order.get('total')}")
        print(f"Tax (5%): Rs.{order.get('tax')}")
        print(f"Amount to pay: Rs.{order.get('grand_total')}")
        print("==============================\n")
