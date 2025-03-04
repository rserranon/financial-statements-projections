# balance_sheet.py
from model_singleton import ModelSingleton
from global_state import GlobalState
from pnl import Revenue

model = ModelSingleton.get_instance()  # Get the singleton instance
initial_year = GlobalState().get('initial_year') 

def Operating_Cash(t):
    """Operating Cash - Minimum cash to mantain the operation"""

    try:
        # Access the 'Operating Cash' ratio row and year `t` column 
        operating_cash_as_revenue = model.Input.Assumptions['Operating Cash'][t]
    except KeyError as e:
        print(f"Error accessing 'Operating Cash' for year {t}: {e}")
        operating_cash_as_revenue = 0 

    return Revenue(t) * (1 + operating_cash_as_revenue)  # Get Operating Cash as % of Revenue 

def Accounts_Receivable(t):
    """Accounts Receivable - level of account receivable as % of revenue"""

    try:
        # Access the 'Operating Cash' ratio row and year `t` column 
        accounts_receivable_as_revenue = model.Input.Assumptions['Accounts Receivable'][t]
    except KeyError as e:
        print(f"Error accessing 'Accounts Receivable' for year {t}: {e}")
        accounts_receivable_as_revenue = 0 

    return Revenue(t) * (1 + accounts_receivable_as_revenue)  # get AR as % of Revenue

def Inventories(t):
    """Inventories - Level of Inventories as % of Revenues"""

    try:
        # Access the 'Operating Cash' ratio row and year `t` column 
        inventories_as_pct_revenue = model.Input.Assumptions['Operating Cash'][t]
    except KeyError as e:
        print(f"Error accessing 'Operating Cash' for year {t}: {e}")
        inventories_as_pct_revenue = 0 

    return Revenue(t) * (1 + inventories_as_pct_revenue)  # Get Operating Cash as % of Revenue 


def Other_Current_Assets(t):
    """Other Current Assets - Level of Other Current Assets as % of Revenues"""

    try:
        # Access the 'Operating Cash' ratio row and year `t` column 
        other_current_assets_as_pct_revenue = model.Input.Assumptions['Other Current Assets'][t]
    except KeyError as e:
        print(f"Error accessing 'Other Current Assets' for year {t}: {e}")
        other_current_assets_as_pct_revenue = 0 

    return Revenue(t) * (1 + other_current_assets_as_pct_revenue)  # Get Other Current Assets as % of Revenue 

def Current_Assets(t):
    """Current assets"""
    return Operating_Cash(t) + Accounts_Receivable(t) + Inventories(t) + Other_Current_Assets(t)

def Non_Current_Assets(t):
    """Non-current assets (long-term assets)"""
    return 120  # Example constant value

def Current_Liabilities(t):
    """Current liabilities"""
    return 60  # Example constant value

def Long_Term_Liabilities(t):
    """Long-term liabilities"""
    return 100  # Example constant value

def Equity(t):
    """Equity, calculated as Assets - Liabilities"""
    return Current_Assets(t) + Non_Current_Assets(t) - Current_Liabilities(t) - Long_Term_Liabilities(t)
