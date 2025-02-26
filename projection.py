import pandas as pd
import matplotlib.pyplot as plt
from build_model import build  # Import the build function from the build_model.py
from global_state import GlobalState

# Set pandas to display all columns in the console
pd.set_option('display.width', None)  # Disable line wrapping
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.max_rows', None)  # Show all rows (optional)

def print_and_plot(df, title, xlabel, ylabel, ax):
    """Function to print and plot the data for a given financial component."""
    print(f"\n Financial Statements: {title}")
    
    # Format each column with commas and round to 2 decimal places
    formatted_df = df.apply(lambda col: col.map(lambda x: f"{x:,.2f}"))
    print(formatted_df.T)  # Transpose for better presentation

    df.plot(title=title, xlabel=xlabel, ylabel=ylabel, grid=True, ax=ax)

def print_and_plot_pnl(model, years, ax):
    """Print and plot the P&L data."""
    vars_pnl = [
        'Revenue', 'COGS', 'SG&A', 'EBIT', 'Interests', 'Taxes', 'EBITDA', 'EBITA', 'NOPAT', 'Net_Income'
    ]
    
    # Collect P&L data
    data_pnl = {var: [model.cells[var](t) for t in years] for var in vars_pnl}
    df_pnl = pd.DataFrame(data_pnl)
    df_pnl['Year'] = years
    df_pnl.set_index('Year', inplace=True)

    # Print and plot
    print_and_plot(df_pnl, "P&L Variables Over Time", "Time Step", "Value", ax)

def print_and_plot_balance_sheet(model, years, ax):
    """Print and plot the Balance Sheet data."""
    vars_balance = [
        'Current_Assets', 'Non_Current_Assets', 'Current_Liabilities', 
        'Long_Term_Liabilities', 'Equity'
    ]
    
    # Collect Balance Sheet data
    data_balance = {var: [model.cells[var](t) for t in years] for var in vars_balance}
    df_balance = pd.DataFrame(data_balance)
    df_balance['Year'] = years
    df_balance.set_index('Year', inplace=True)

    # Print and plot
    print_and_plot(df_balance, "Balance Sheet Variables Over Time", "Time Step", "Value", ax)

def print_and_plot_cashflow(model, years, ax):
    """Print and plot the Cash Flow data."""
    vars_cashflow = [
        'Operating_CashFlow', 'Investing_CashFlow', 'Financing_CashFlow', 'Net_CashFlow'
    ]
    
    # Collect Cash Flow data
    data_cashflow = {var: [model.cells[var](t) for t in years] for var in vars_cashflow}
    df_cashflow = pd.DataFrame(data_cashflow)
    df_cashflow['Year'] = years
    df_cashflow.set_index('Year', inplace=True)

    # Print and plot
    print_and_plot(df_cashflow, "Cash Flow Variables Over Time", "Time Step", "Value", ax)

def run_projection():
    # Initialize values
    GlobalState().set('initial_year', 2025)  # Set the initial year
    GlobalState().set('projection_span', 10)  # Set the projection span
    # Define the period range (e.g., 2025 to 2034)
    proj_span = GlobalState().get('projection_span')  
    initial_year = GlobalState().get('initial_year')
    years = range(initial_year, initial_year + proj_span)

    # Build the model using the build function from build_model.py
    model = build()
    print("Model built successfully!")


    # Set up the subplots for P&L, Balance Sheet, and Cash Flow
    fig, axs = plt.subplots(3, 1, figsize=(10, 8))  # 3 rows, 1 column

    # Set pandas to display all columns
    pd.set_option('display.max_columns', None)

    # Print and plot each financial component (P&L, Balance Sheet, Cash Flow) in different subplots
    print_and_plot_pnl(model, years, axs[0])
    print_and_plot_balance_sheet(model, years, axs[1])
    print_and_plot_cashflow(model, years, axs[2])

    # Adjust layout for better spacing between subplots
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    run_projection()
