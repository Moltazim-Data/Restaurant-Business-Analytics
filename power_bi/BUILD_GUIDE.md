# Power BI Dashboard Build Guide

## 1. Load data
Import the CSV files from `data/processed/`: `sales_daily.csv`, `menu_performance.csv`, `sales_by_hour.csv`, `category_performance.csv` and `staffing_by_hour.csv`. For drill-through and channel analysis, also import raw `orders.csv` and `order_items.csv`.

## 2. Model
Use `orders[order_id]` (one) to `order_items[order_id]` (many), and `menu_items[menu_item_id]` (one) to `order_items[menu_item_id]` (many), if importing the raw tables. Keep date fields typed as Date and EUR amounts as Decimal Number.

## 3. Suggested report pages
- Executive Overview: net sales, orders, AOV, estimated food gross profit and margin; monthly trend and channel mix.
- Menu Performance: item/category sales, units, estimated gross profit and margin; scatter plot of popularity vs margin.
- Demand & Staffing: order volume and sales by hour/weekday with planned vs observed staffing.

## 4. Measures
Use the measures in `DAX_Measures.dax`. Confirm relationships and avoid summing pre-aggregated totals alongside raw line-level data.

## 5. Interpretation
Gross profit in this case study deducts estimated food cost only. It is not operating profit. All data and outputs are synthetic.
