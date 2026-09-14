"""
Module: Lightweight Production KPI Visualizer
Generates ASCII-based terminal visualizations without external dependencies.
"""

from typing import List, Dict


def plot_ascii_bar_chart(data: Dict[str, int]) -> None:
    """Generate a clean ASCII bar chart in the terminal."""
    print("\n📊 MACHINE DOWNTIME VISUALIZATION (MINUTES):")
    print("-" * 55)
    max_val = max(data.values()) if data else 1

    for machine, minutes in data.items():
        # Scale the bar length up to 30 characters
        bar_length = int((minutes / max_val) * 30) if max_val > 0 else 0
        bar = "█" * bar_length
        print(f"{machine.ljust(12)} | {bar.ljust(30)} {minutes} mins")
    print("-" * 55)


def main():
    downtime_data = {
        "Machine 1": 12,
        "Machine 2": 45,
        "Machine 3": 0,
        "Machine 4": 8,
        "Machine 5": 120,
    }

    plot_ascii_bar_chart(downtime_data)
    print("✅ Pure Python ASCII Visualization executed successfully!")


if __name__ == "__main__":
    main()
