# Smart Inventory Reorder Engine - Simple Version
# Author: Behnoosh Akbari

# Warehouse data: each item is a dictionary
inventory = [
    {"name": "Ball Bearing 6205", "stock": 18, "daily_use": 4, "lead_time": 5},
    {"name": "Timing Belt HTD",   "stock": 5,  "daily_use": 3, "lead_time": 10},
    {"name": "Proximity Sensor",  "stock": 65, "daily_use": 2, "lead_time": 14},
]

print("=" * 50)
print("SMART INVENTORY CHECKER")
print("=" * 50)

for item in inventory:
    # Reorder Point = daily use * delivery time + small safety buffer
    rop = item["daily_use"] * item["lead_time"]

    if item["stock"] <= rop:
        print(f"RED   | {item['name']}: stock {item['stock']}, ROP {rop} -> ORDER NOW!")
    else:
        print(f"GREEN | {item['name']}: stock {item['stock']}, ROP {rop} -> OK")

print("=" * 50)
