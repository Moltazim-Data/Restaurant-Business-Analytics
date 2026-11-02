# Data Dictionary

## Raw data

### `orders.csv`
One row per fictional order. `order_id` is the primary key; `order_date`, `order_time`, `weekday`, `month` and `hour` describe timing; `order_channel`, `order_type` and `payment_method` describe fulfilment/payment; `customer_id` is a synthetic identifier; `order_subtotal_eur` is the order subtotal.

### `order_items.csv`
One row per order line. `order_line_id` is the primary key; `order_id` links to orders; `menu_item_id` links to menu items; `quantity`, `unit_price_eur`, `gross_sales_eur`, `discount_eur`, `net_sales_eur`, `unit_food_cost_eur`, `food_cost_eur` and `gross_profit_eur` describe the line.

### `menu_items.csv`
One row per menu item. Includes item name, category, list price, unit food cost and target food-cost percentage.

### `staffing_by_hour.csv`
One row per date/hour with observed and planned staff counts.

## Processed data
- `sales_daily.csv`: daily sales, food cost, gross profit, units, orders and margin.
- `menu_performance.csv`: item-level volume, revenue, estimated food cost and gross profit.
- `sales_by_hour.csv`: hourly sales, orders and units by date and weekday.
- `category_performance.csv`: category-level sales and estimated profitability.
- `staffing_by_hour.csv`: staffing observations retained for dashboard analysis.

Currency is EUR. Percentages are stored as decimal fractions unless otherwise noted. Data is synthetic.
