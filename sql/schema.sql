-- Example analytical schema (PostgreSQL)
CREATE TABLE orders (
  order_id TEXT PRIMARY KEY, order_date DATE, order_time TIME,
  weekday TEXT, month INTEGER, hour INTEGER, order_channel TEXT,
  order_type TEXT, payment_method TEXT, customer_id TEXT,
  order_subtotal_eur NUMERIC(12,2)
);
CREATE TABLE menu_items (
  menu_item_id TEXT PRIMARY KEY, item_name TEXT, category TEXT,
  list_price_eur NUMERIC(10,2), unit_food_cost_eur NUMERIC(10,2),
  target_food_cost_pct NUMERIC(6,4)
);
CREATE TABLE order_items (
  order_line_id TEXT PRIMARY KEY, order_id TEXT REFERENCES orders(order_id),
  menu_item_id TEXT REFERENCES menu_items(menu_item_id), item_name TEXT,
  category TEXT, quantity INTEGER, unit_price_eur NUMERIC(10,2),
  gross_sales_eur NUMERIC(12,2), discount_eur NUMERIC(12,2),
  net_sales_eur NUMERIC(12,2), unit_food_cost_eur NUMERIC(10,2),
  food_cost_eur NUMERIC(12,2), gross_profit_eur NUMERIC(12,2)
);
