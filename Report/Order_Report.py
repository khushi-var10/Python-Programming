from Model.Order_Model import OrderModel

class OrderReport:
    def show_all_orders(self):
        ordermodel = OrderModel()
        orders = ordermodel.load_orders()
        if not orders:
            print("\nERROR: No orders have been placed yet. Order list is empty.\n")
            return
        print("\n===== ALL ORDERS =====")
        for o in orders:
            print(f"\nOrder ID: {o.get('id')}  Date: {o.get('date')}  By: {o.get('receptionist')}")
            for it in o.get("items", []):
                print(f" - {it.get('name')} ({it.get('size')}) x{it.get('qty')} = Rs.{it.get('subtotal')}")
            print(f"Total: Rs.{o.get('total')}  Tax: Rs.{o.get('tax')}  Grand: Rs.{o.get('grand_total')}")
        print()
