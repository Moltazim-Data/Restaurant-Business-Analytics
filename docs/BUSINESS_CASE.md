# Business Case: Restaurant Performance Analytics

## Scenario
A fictional casual-dining restaurant wants a clearer view of sales performance, menu contribution, ordering patterns and staffing coverage. Management needs a repeatable reporting workflow rather than disconnected spreadsheets.

## Objectives
- Monitor net sales, order volume and average order value.
- Compare menu items and categories by volume, revenue and estimated food gross profit.
- Identify demand patterns by weekday and hour.
- Compare hourly staffing levels with demand as an initial operational diagnostic.
- Provide documented, reproducible data preparation for a Power BI dashboard.

## Scope
The case study uses generated transaction, menu and hourly staffing data for calendar year 2025. Python performs validation and aggregation; SQL provides example analytical questions; Power BI is the intended reporting layer.

## KPI definitions
- Net sales: line-level sales after discounts.
- Food cost: estimated ingredient cost for items sold.
- Gross profit: net sales less estimated food cost.
- Gross margin: gross profit divided by net sales.
- Average order value: order subtotal average.

Gross profit is not operating profit. The model excludes labour cost, rent, utilities, taxes, delivery commissions, waste and other overheads. Staffing counts are not payroll costs.

## Important limitation
All businesses, customers, orders, costs and results are synthetic. Figures are for portfolio demonstration only and must not be presented as actual client results.
