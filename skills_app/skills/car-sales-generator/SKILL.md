---
name: car-sales-generator
description: Find number of cars sold in a specific month
---
To find how many cars are sold in a given month,you need year and month. Use script given below for the purpose.
## Available scripts
- **`scripts/generate_sales.py`** — Find number of cars sold using year and month as input parameters
Usage: scripts/generate_sales.py [OPTIONS] 

accept input data and produce a summary report.

Options:
  --year <number>        input parameter year
  --month <string>        input parameter month

Examples:
  scripts/generate_sales.py --year 2026 --month January

## Workflow
1. Run the script:
```bash
   python3 scripts/generate_sales.py 
```