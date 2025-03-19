# balance_sheet.py
from model_singleton import ModelSingleton
from global_state import GlobalState
from pnl import Revenue
from utils import get_assumption_value

model = ModelSingleton.get_instance()  # Get the singleton instance
initial_year = GlobalState().get('initial_year') 


def Operating_Cash(t):
    """Operating Cash - Minimum cash to maintain the operation"""
    operating_cash_as_revenue = get_assumption_value(model, 'Operating Cash', t)
    return Revenue(t) * (1 + operating_cash_as_revenue)

def Accounts_Receivable(t):
    """Accounts Receivable - level of account receivable as % of revenue"""
    accounts_receivable_as_revenue = get_assumption_value(model, 'Accounts Receivable', t)
    return Revenue(t) * (1 + accounts_receivable_as_revenue)

def Inventories(t):
    """Inventories - Level of Inventories as % of Revenues"""
    inventories_as_pct_revenue = get_assumption_value(model, 'Inventories', t)  # Corrected category to 'Inventories'
    return Revenue(t) * (1 + inventories_as_pct_revenue)

def Other_Current_Assets(t):
    """Other Current Assets - Level of Other Current Assets as % of Revenues"""
    other_current_assets_as_pct_revenue = get_assumption_value(model, 'Other Current Assets', t)
    return Revenue(t) * (1 + other_current_assets_as_pct_revenue)

def Current_Assets(t):
    """Current assets"""
    return (Operating_Cash(t) + Accounts_Receivable(t) +
            Inventories(t) + Other_Current_Assets(t))

def Non_Current_Assets(t):
    """Non-current assets (long-term assets)"""
    return 120  # Example constant value

def Accounts_Payable(t):
    """Accounts Payable - Level of Accounts Payable as % of Revenues"""
    accounts_payable_as_pct_revenue = get_assumption_value(model, 'Accounts Payable', t)
    return Revenue(t) * (1 + accounts_payable_as_pct_revenue)

def Other_Current_Liabilities(t):
    """Other Current Liabilities - Level of Other Current Liabilities as % of Revenues"""
    other_current_liabilities_as_pct_revenue = get_assumption_value(model, 'Other Current Liabilities', t)
    return Revenue(t) * (1 + other_current_liabilities_as_pct_revenue)

def Current_Liabilities(t):
    """Current liabilities"""
    return Accounts_Payable(t) + Other_Current_Liabilities(t)

def Long_Term_Liabilities(t):
    """Long-term liabilities"""
    return 100  # Example constant value

def Equity(t):
    """Equity, calculated as Assets - Liabilities"""
    return (Current_Assets(t) + Non_Current_Assets(t) -
            Current_Liabilities(t) - Long_Term_Liabilities(t))
