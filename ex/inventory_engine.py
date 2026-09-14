# Smart Inventory Reorder & EOQ Engine
# Author: Behnoosh Akbari | Industrial Engineer
import math

inventory = [
    {
        "name": "Ball Bearing 6205",
        "stock": 18,
        "daily_use": 4,
        "lead_time": 5,
        "annual_demand": 1400,
        "order_cost": 45,       # هزینه سفارش‌دهی به ازای هر بار ($)
        "holding_cost": 3.5     # هزینه نگهداری هر واحد در سال ($)
    },
    {
        "name": "Timing Belt HTD",
        "stock": 5,
        "daily_use": 3,
        "lead_time": 10,
        "annual_demand": 800,
        "order_cost": 30,
        "holding_cost": 2.0
    },
    {
        "name": "Proximity Sensor",
        "stock": 65,
        "daily_use": 2,
        "lead_time": 14,
        "annual_demand": 400,
        "order_cost": 50,
        "holding_cost": 5.0
    }
]

print("=" * 65)
print("📦 SMART INVENTORY & EOQ OPTIMIZER")
print("=" * 65)

for item in inventory:
    # 1. محاسبه نقطه سفارش مجدد (ROP)
    rop = item["daily_use"] * item["lead_time"]
    
    # 2. محاسبه مقدار سفارش اقتصادی (EOQ) فرمول ویلسون
    eoq = math.isqrt(int((2 * item["annual_demand"] * item["order_cost"]) / item["holding_cost"]))

    # 3. بررسی وضعیت موجودی
    if item["stock"] <= rop:
        print(f"🔴 [REORDER] {item['name']:<20} | Stock: {item['stock']:<3} | ROP: {rop:<3} -> Order EOQ: {eoq} units!")
    else:
        print(f"🟢 [OPTIMAL] {item['name']:<20} | Stock: {item['stock']:<3} | ROP: {rop:<3} -> Stock is Healthy.")

print("=" * 65)
