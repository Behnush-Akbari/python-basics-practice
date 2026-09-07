
"""
Module: Inventory KPI Calculator
Calculates Economic Order Quantity (EOQ) and Reorder Point (ROP)
for industrial supply chain management.
"""

import math


def calculate_eoq(demand: float, order_cost: float, holding_cost: float) -> float:
    """Calculate the Economic Order Quantity (EOQ)."""
    if holding_cost <= 0:
        raise ValueError("Holding cost must be greater than zero.")
    return math.sqrt((2 * demand * order_cost) / holding_cost)


def calculate_rop(daily_demand: float, lead_time_days: int, safety_stock: int = 0) -> float:
    """Calculate the Reorder Point (ROP)."""
    return (daily_demand * lead_time_days) + safety_stock


def check_inventory_status(current_stock: int, rop: float) -> str:
    """Evaluate current stock level against Reorder Point."""
    if current_stock <= rop:
        return f"🚨 WARNING: Current stock ({current_stock}) is at or below ROP ({rop:.2f}). Place an order immediately!"
    return f"✅ OK: Stock level ({current_stock}) is sufficient (ROP: {rop:.2f})."


def main():
    print("=" * 45)
    print("📊 INVENTORY KPI & EOQ SYSTEM")
    print("=" * 45)

    # Business Parameters (e.g., Automotive spare parts)
    annual_demand = 12000.0      # D: 12,000 units/year
    cost_per_order = 50.0        # S: 50 € per order
    holding_cost_unit = 2.5      # H: 2.5 € per unit/year
    
    lead_time_days = 5           # L: 5 days lead time
    daily_demand = annual_demand / 365
    current_inventory = 140      # Current warehouse units

    # Calculations
    eoq_value = calculate_eoq(annual_demand, cost_per_order, holding_cost_unit)
    rop_value = calculate_rop(daily_demand, lead_time_days, safety_stock=20)
    status = check_inventory_status(current_inventory, rop_value)

    # Output Report
    print(f"Optimal Order Quantity (EOQ): {eoq_value:.2f} units")
    print(f"Reorder Point (ROP):         {rop_value:.2f} units")
    print("-" * 45)
    print(f"Status: {status}")
    print("=" * 45)


if __name__ == "__main__":
    main()
