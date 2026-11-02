from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'data' / 'raw'
OUT = ROOT / 'data' / 'processed'

def load_data():
    return (
        pd.read_csv(RAW / 'orders.csv', parse_dates=['order_date']),
        pd.read_csv(RAW / 'order_items.csv'),
        pd.read_csv(RAW / 'menu_items.csv'),
        pd.read_csv(RAW / 'staffing_by_hour.csv', parse_dates=['date']),
    )

def validate_data(orders, items, menu, staffing):
    checks = {
        'unique_orders': orders.order_id.is_unique,
        'unique_lines': items.order_line_id.is_unique,
        'valid_order_keys': items.order_id.isin(orders.order_id).all(),
        'valid_menu_keys': items.menu_item_id.isin(menu.menu_item_id).all(),
        'nonnegative_sales': (items.net_sales_eur >= 0).all(),
        'positive_quantity': (items.quantity > 0).all(),
        'nonnegative_costs': (items.food_cost_eur >= 0).all(),
        'nonnegative_staff': (staffing.staff_on_shift >= 0).all(),
    }
    if not all(checks.values()):
        raise ValueError({key: value for key, value in checks.items() if not value})
    return checks

def build_outputs(orders, items, menu, staffing):
    OUT.mkdir(parents=True, exist_ok=True)
    joined = items.merge(orders[['order_id', 'order_date', 'weekday', 'month', 'hour']], on='order_id')
    daily = joined.groupby(['order_date', 'weekday', 'month'], as_index=False).agg(
        net_sales_eur=('net_sales_eur', 'sum'), food_cost_eur=('food_cost_eur', 'sum'),
        gross_profit_eur=('gross_profit_eur', 'sum'), units_sold=('quantity', 'sum'),
        order_count=('order_id', 'nunique'))
    daily['gross_margin_pct'] = daily.gross_profit_eur / daily.net_sales_eur
    performance = items.groupby(['menu_item_id', 'item_name', 'category'], as_index=False).agg(
        units_sold=('quantity', 'sum'), net_sales_eur=('net_sales_eur', 'sum'),
        food_cost_eur=('food_cost_eur', 'sum'), gross_profit_eur=('gross_profit_eur', 'sum'))
    performance['gross_margin_pct'] = performance.gross_profit_eur / performance.net_sales_eur
    performance = performance.merge(menu, on='menu_item_id')
    hourly = joined.groupby(['order_date', 'hour', 'weekday'], as_index=False).agg(
        net_sales_eur=('net_sales_eur', 'sum'), order_count=('order_id', 'nunique'),
        units_sold=('quantity', 'sum'))
    category = items.groupby('category', as_index=False).agg(
        units_sold=('quantity', 'sum'), net_sales_eur=('net_sales_eur', 'sum'),
        food_cost_eur=('food_cost_eur', 'sum'), gross_profit_eur=('gross_profit_eur', 'sum'))
    category['gross_margin_pct'] = category.gross_profit_eur / category.net_sales_eur
    outputs = {'sales_daily.csv': daily, 'menu_performance.csv': performance,
               'sales_by_hour.csv': hourly, 'category_performance.csv': category,
               'staffing_by_hour.csv': staffing}
    for filename, frame in outputs.items():
        frame.to_csv(OUT / filename, index=False)
    return {name: len(frame) for name, frame in outputs.items()}

if __name__ == '__main__':
    orders, items, menu, staffing = load_data()
    print('Validation:', validate_data(orders, items, menu, staffing))
    print('Outputs:', build_outputs(orders, items, menu, staffing))
