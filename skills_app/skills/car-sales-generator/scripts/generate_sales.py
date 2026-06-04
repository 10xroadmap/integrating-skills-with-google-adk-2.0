# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pandas"
# ]
# ///

import sys
import json
import argparse
import pandas as pd
def generate_car_sales(year, month):
    df = pd.read_csv("car-sales.csv")
    result = df.query(f"year == {year} and month = '{month}")
    return result['sales']

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate car sales .')
    parser.add_argument('--year', type=str, help='input parameter year')
    parser.add_argument('--month', type=str, help='input parameter month')
    args, unknown = parser.parse_known_args()
    # Fallback to positional if flags are not used, to be safe
    year = args.year
    month = args.month
    if not year or not month:
        if len(sys.argv) >= 3:
            year = sys.argv[1]
            month = sys.argv[2]
        else:
            print(json.dumps({"error": "Missing arguments. Usage: --year <year> --month <month>"}))
            sys.exit(1)         
    print(generate_car_sales(year, month))


