# Restaurant Business Analytics

A professional end-to-end restaurant analytics case study using synthetic data, Python, SQL and Power BI.

## Business context
This project models a fictional casual dining restaurant. It demonstrates a repeatable workflow for validating transaction data, measuring sales and estimated food profitability, evaluating menu performance and analysing hourly demand alongside staffing.

## Dataset
The synthetic dataset covers 1 January–31 December 2025 and includes 10,385 orders, 25,639 order lines, 18 menu items and 4,380 hourly staffing records. All records are generated for demonstration; they are not actual client or restaurant data.

## Demonstration snapshot
- Net sales: **€262,899.90**
- Estimated food cost: **€75,134.78**
- Gross profit after estimated food cost: **€187,765.12**
- Gross margin: **71.42%**
- Average order value: **€25.32**

Gross profit here subtracts estimated food cost only. It does not include labour, rent, utilities, taxes, delivery commissions, waste or other overheads. These figures are not audited financial results.

## Repository structure
```text
data/raw/          Synthetic source CSV files
data/processed/    Aggregated analysis outputs
docs/              Business case and data dictionary
power_bi/          Dashboard build guide and DAX measures
reports/           Initial profile and findings
sql/               SQL schema and business questions
src/               Python analysis and KPI scripts
tests/             Data quality tests
```

## Run locally
```bash
python -m pip install -r requirements.txt
python src/analysis.py
python src/kpi_summary.py
python -m pytest -q
```

The analysis script reads source CSV files from `data/raw/` and writes reproducible summary tables into `data/processed/`.

## Power BI
Follow `power_bi/BUILD_GUIDE.md` to import the processed CSV outputs, create relationships and build the report. DAX measures are in `power_bi/DAX_Measures.dax`.

## Methodology and limitations
The source records are synthetic. Ingredient costs and staffing observations are scenario assumptions, not accounting or payroll records. Validate assumptions against real data before using any analysis in operational decisions.

## Author
Abdelhamid Moltazim | [GitHub](https://github.com/Moltazim-Data) | [LinkedIn](https://www.linkedin.com/in/abdelhamid-moltazim) | [Portfolio](https://moltazimdata.com)
