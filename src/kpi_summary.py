from analysis import load_data, validate_data

orders, items, menu, staffing = load_data()
validate_data(orders, items, menu, staffing)
sales = items.net_sales_eur.sum()
food_cost = items.food_cost_eur.sum()
profit = items.gross_profit_eur.sum()
print(f'Net sales: EUR {sales:,.2f}')
print(f'Food cost: EUR {food_cost:,.2f}')
print(f'Gross profit: EUR {profit:,.2f}')
print(f'Gross margin: {profit / sales:.1%}')
print(f'Orders: {orders.order_id.nunique():,}')
print(f'Average order value: EUR {orders.order_subtotal_eur.mean():.2f}')
