-- 1. Sales and order volume by channel
SELECT o.order_channel, COUNT(DISTINCT o.order_id) AS orders,
       SUM(i.net_sales_eur) AS net_sales_eur
FROM orders o JOIN order_items i USING (order_id)
GROUP BY o.order_channel ORDER BY net_sales_eur DESC;

-- 2. Menu-item profitability
SELECT menu_item_id, item_name, SUM(quantity) AS units_sold,
       SUM(net_sales_eur) AS net_sales_eur,
       SUM(gross_profit_eur) AS estimated_food_gross_profit_eur,
       SUM(gross_profit_eur) / NULLIF(SUM(net_sales_eur),0) AS gross_margin
FROM order_items GROUP BY menu_item_id, item_name
ORDER BY estimated_food_gross_profit_eur DESC;

-- 3. Demand by hour
SELECT o.hour, COUNT(DISTINCT o.order_id) AS orders,
       SUM(i.net_sales_eur) AS net_sales_eur
FROM orders o JOIN order_items i USING (order_id)
GROUP BY o.hour ORDER BY o.hour;

-- 4. Daily sales trend
SELECT o.order_date, COUNT(DISTINCT o.order_id) AS orders,
       SUM(i.net_sales_eur) AS net_sales_eur
FROM orders o JOIN order_items i USING (order_id)
GROUP BY o.order_date ORDER BY o.order_date;
