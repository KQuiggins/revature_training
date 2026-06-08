"""
Week 2 Exercise — CSV processing with context managers.

TODO:
1. Read starter_code/data/sales.csv using csv.DictReader and with open(...).
2. Compute rows count, grand total (sum of units * unit_price), average line revenue.
3. Find SKU with max line revenue (tie: first in file).
4. Write output/summary.txt using with open(..., "w", encoding="utf-8").
"""

from __future__ import annotations
import csv
import sys

def main() -> None:

    rows = 0
    bad_rows = 0
    grand_total = 0
    top_sku = None
    top_line_revenue = 0

    with open("data/sales.csv", mode="r", encoding="utf-8") as file:
        reader=csv.DictReader(file)

        for line_number, row in enumerate(reader):
            try:
                row["units"] = int(row["units"])
                row["unit_price"] = float(row["unit_price"])
                print(row)

                # Calculate revenue
                line_revenue = row["units"] * row["unit_price"]

                rows+=1
                grand_total+=line_revenue

                if line_revenue > top_line_revenue:
                    top_line_revenue = line_revenue
                    top_sku = row["sku"]

            except (ValueError, KeyError, TypeError) as e:
                bad_rows+=1

                print(f"Bad row {line_number}: {e}")
                file=sys.stderr

    print(f"{bad_rows}", file=sys.stderr )



    average_line_revenue = (
        grand_total / rows if rows else 0
    )

    with open(
        "output/summary.txt",
        mode="w",
        encoding="utf-8"
    ) as summary_file:

        summary_file.write(f"rows={rows}\n")
        summary_file.write(f"grand_total={grand_total:.2f}\n")
        summary_file.write(f"average_line_revenue={average_line_revenue:.2f}\n")
        summary_file.write(f"top_sku={top_sku}\n")
        summary_file.write(f"top_line_revenue={top_line_revenue:.2f}\n")

if __name__ == "__main__":
    main()