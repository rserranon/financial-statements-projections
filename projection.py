# projection.py
import pandas as pd
import matplotlib.pyplot as plt
from build_model import build  # Import the build function from the build_model.py

def run_projection():
    # Build the model using the build function from build_model.py
    model = build()
    print("Model built successfully!")

    # ------------------------------------------------------------------------
    # Access cells dynamically (e.g., P&L, Balance Sheet, Cash Flow)
    vars = [
        'Revenue', 'COGS', 'Operating_Expenses', 'Net_Income',
        'Current_Assets', 'Non_Current_Assets', 'Current_Liabilities', 'Long_Term_Liabilities', 'Equity',
        'Operating_CashFlow', 'Investing_CashFlow', 'Financing_CashFlow', 'Net_CashFlow'
    ]

    # Define the period range (e.g., 2025 to 2034)
    proj_span = 10  # 10 years for projection
    years = range(2025, 2025 + proj_span)

    # Modify the data dictionary to include 'years' as the index or a column
    data = {var: [model.cells[var](t) for t in years] for var in vars}

    # Now add the years as a column in the DataFrame
    df = pd.DataFrame(data)

    # Add 'Year' column with the actual years
    df['Year'] = years

    # Optionally, you can set 'Year' as the index if desired
    df.set_index('Year', inplace=True)

    # Print the resulting DataFrame
    print(df.T)
    
    # Optionally, plot the variables over time
    df.plot(title="Financial Statements Variables Over Time", xlabel="Time Step", ylabel="Value", grid=True)
    plt.show()

if __name__ == '__main__':
    run_projection()

