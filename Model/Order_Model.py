import json
import os
import datetime

ORDER_FILE = os.path.join("Database", "order.json")

class OrderModel:
    def load_orders(self):
        try:
            if not os.path.exists(ORDER_FILE):
                return []
            with open(ORDER_FILE, "r") as file:
                return json.load(file)
        except Exception:
            return []

    def save_orders(self, data):
        with open(ORDER_FILE, "w") as file:
            json.dump(data, file, indent=2)

    def add_order(self, order_data):
        orders = self.load_orders()
        order_data["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ids = [o.get("id", 0) for o in orders]
        order_data["id"] = max(ids, default=0) + 1
        orders.append(order_data)
        self.save_orders(orders)
        return order_data
