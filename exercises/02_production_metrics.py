"""
Module: Production Line Metrics & Downtime Analysis
Analyzes equipment downtime and computes availability KPIs.
"""

from typing import List, Dict

SHIFT_DURATION_MINUTES = 480  # Standard 8-hour shift


def calculate_total_downtime(downtimes: List[int]) -> int:
    """Calculate total downtime in minutes."""
    return sum(downtimes)


def calculate_active_downtime_average(downtimes: List[int]) -> float:
    """Calculate mean downtime excluding zero-downtime machines."""
    active_failures = [dt for dt in downtimes if dt > 0]
    if not active_failures:
        return 0.0
    return sum(active_failures) / len(active_failures)


def calculate_availability_kpi(downtimes: List[int]) -> Dict[str, float]:
    """Calculate Availability Percentage (KPI) for each machine."""
    availability = {}
    for idx, dt in enumerate(downtimes, start=1):
        machine_name = f"Machine_{idx}"
        operating_time = SHIFT_DURATION_MINUTES - dt
        avail_percent = (operating_time / SHIFT_DURATION_MINUTES) * 100
        availability[machine_name] = round(avail_percent, 2)
    return availability


def main():
    print("=" * 50)
    print("🏭 PRODUCTION LINE DOWNTIME REPORT")
    print("=" * 50)

    # Machine downtime in minutes for Shift 1
    downtimes = [12, 45, 0, 8, 120]

    total_dt = calculate_total_downtime(downtimes)
    avg_dt = calculate_active_downtime_average(downtimes)
    machine_kpis = calculate_availability_kpi(downtimes)

    print(f"Total Downtime:           {total_dt} mins")
    print(f"Average (Active Failures): {avg_dt:.1f} mins")
    print("-" * 50)
    print("Machine Availability Breakdown:")
    for machine, avail in machine_kpis.items():
        print(f"  • {machine}: {avail}%")
    print("=" * 50)


if __name__ == "__main__":
    main()
