from Model.Order_Model import OrderModel
from collections import defaultdict

class RevenueReport:
    def show_revenue(self):
        ordermodel = OrderModel()
        orders = ordermodel.load_orders()
        if not orders:
            print("\nERROR: No revenue data — no orders placed yet.\n")
            return
        total_revenue = sum(o.get("grand_total", 0) for o in orders)
        by_date = defaultdict(float)
        for o in orders:
            date = o.get("date", "").split()[0]
            by_date[date] += o.get("grand_total", 0)
        print("\n===== REVENUE REPORT =====")
        print(f"Total Revenue (all time): Rs.{total_revenue}")
        print("\nRevenue by date:")
        for d, amt in sorted(by_date.items()):
            print(f"{d}: Rs.{amt}")
        print()
