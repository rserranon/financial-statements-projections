# Financial Projections Model

This project implements a financial projection model for generating projected financial statements, such as Profit & Loss (P&L), Balance Sheet, and Cash Flow statements. The model allows for customizable growth rates, ratio assumptions, and the ability to calculate financial variables for multiple periods. The projections are based on initial data and assumptions that can vary by period.

## Modules and versions

- **Pandas**:  
  ![Pandas Version](https://img.shields.io/pypi/v/pandas.svg)
  ![Pandas Current Version](https://img.shields.io/pypi/v/pandas.svg)

- **Matplotlib**:  
  ![Matplotlib Version](https://img.shields.io/pypi/v/matplotlib.svg)
  ![Matplotlib Current Version](https://img.shields.io/pypi/v/matplotlib.svg)

- **ModelX**:  
  ![ModelX Version](https://img.shields.io/badge/modelx-0.20.0-blue)
![ModelX Current Version](https://img.shields.io/pypi/v/modelx.svg)

- **Python**:  
  [![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)

- **License** (e.g., MIT):  
  ![GitHub License](https://img.shields.io/github/license/rserranon/financial-statements-projections)

## Project Architecture

The project is organized into separate modules, each responsible for a specific section of the model. The following structure is used to keep the project modular and maintainable:

### File Structure

```bash
financial-projections/
├── build_model.py        # Function to build the financial model
├── projections.py        # Main script to run projections
├── pnl.py                # Module for P&L calculations
├── balance_sheet.py      # Module for Balance Sheet calculations
├── cashflow.py           # Module for Cash Flow calculations
├── assumptions.xlsx      # Excel file for growth and ratio assumptions
└── README.md             # Project documentation
```

### Key Modules

- build_model.py:

Contains the function to build the model by defining various spaces (e.g., P&L, Balance Sheet, Cash Flow).
The function build() creates a model and adds references to cells like Revenue, Operating_Expenses, Net_Income, etc.
Assumptions are dynamically loaded from an Excel file, and space references for all components are established.

- pnl.py:

Defines calculations for the Profit & Loss statement.
Includes functions like Revenue(), COGS(), Operating_Expenses(), and Net_Income() to calculate values based on the given assumptions.

- balance_sheet.py:

Defines the Balance Sheet structure.
Includes functions like Current_Assets(), Non_Current_Assets(), Liabilities(), and Equity() to calculate the various components of the balance sheet.

- cashflow.py:

Defines the Cash Flow statement and the related components.
Includes functions like Operating_CashFlow(), Investing_CashFlow(), and Financing_CashFlow() to calculate the cash flows over time.

- assumptions.xlsx:

An Excel file used to store assumptions for growth rates and ratios for each period (t).
Contains tables such as Revenue Growth, Expense Ratios, and other factors affecting the projections over time.

### Key Functions

1. build_model.py
build(): This function creates spaces (P&L, Balance Sheet, Cash Flow) in the model and sets their respective formulas. It also loads the assumptions dynamically from the assumptions.xlsx file.
2. pnl.py
Revenue(t): Calculates the revenue for period t.
COGS(t): Calculates the Cost of Goods Sold for period t.
Operating_Expenses(t): Calculates operating expenses for period t.
Net_Income(t): Calculates net income by subtracting expenses from revenue for period t.
3. balance_sheet.py
Current_Assets(t): Calculates current assets for period t.
Non_Current_Assets(t): Calculates non-current assets for period t.
Current_Liabilities(t): Calculates current liabilities for period t.
Long_Term_Liabilities(t): Calculates long-term liabilities for period t.
Equity(t): Calculates equity based on assets and liabilities for period t.
4. cashflow.py
Operating_CashFlow(t): Calculates operating cash flow for period t.
Investing_CashFlow(t): Calculates investing cash flow for period t.
Financing_CashFlow(t): Calculates financing cash flow for period t.
Net_CashFlow(t): Calculates net cash flow by summing operating, investing, and financing cash flows for period t.

5. Assumptions File (Excel)
assumptions.xlsx contains assumptions for various factors affecting the model, including growth rates and ratios that can vary by period.
The assumptions are loaded dynamically into the model using the modelx methods like new_pandas() and new_cells_from_excel().
The data is structured with rows representing the different assumptions and columns representing the periods (t).

Example Assumptions table:

Assumption Name Period 1 Period 2 Period 3 ...
Revenue Growth 5% 5% 5% ...
Expense Ratio 10% 9% 8% ...
COGS Ratio 60% 58% 55% ...
Data and Projection Calculation

The data for each period is calculated based on the following:

The initial data at t(0) is provided in the form of basic financial figures (e.g., initial revenue, initial assets, etc.).
Growth and ratio assumptions (e.g., revenue growth, expense ratios) are applied across all periods (t).
The financial statements are projected over a period of time (e.g., 10 years).
The projection is done dynamically by calculating the values for each cell (e.g., Revenue, Operating_Expenses, Net_Income, etc.) for each period using the assumption data loaded from the assumptions.xlsx file.

### Example Usage

#### Building the Model: The model can be built by running the build_model.py script

```bash
python build_model.py
Running Projections: After the model is built, projections can be run by executing the projections.py script:
```

```bash
python projections.py
```

Accessing Results: Once the projections are computed, the results can be accessed through the model's cells attribute and can be used for further analysis or saved to files.

#### Example Code

Here’s an example of how to access the projected data:

```python
# Assuming you have built the model
proj_span = 10  # 10 years for projection
years = range(2025, 2025 + proj_span)

vars = ['Revenue', 'COGS', 'Operating_Expenses', 'Net_Income']

data = {var: [model.cells[var](t) for t in years] for var in vars}

df = pd.DataFrame(data)

# Set 'Year' as index
df['Year'] = years
df.set_index('Year', inplace=True)

# Print the resulting DataFrame
print(df)
```

### Future Enhancements

Scenario Analysis: Implement multiple scenarios by modifying the assumption file and evaluating the model with different assumptions.
Advanced Financial Metrics: Expand the model to include additional financial metrics, such as ratios for profitability, liquidity, and efficiency.
Visualization: Enhance the analysis by adding visualizations for the projections and financial statements over time.
