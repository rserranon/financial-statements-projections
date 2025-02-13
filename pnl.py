# pnl.py
from model_singleton import ModelSingleton
from global_state import GlobalState

def Taxes(t, base):
    """Taxes based on net income"""
    return 0.3 * base  # 30% tax

def Revenue(t):
    """Revenue or Sales"""
    model = ModelSingleton.get_instance()  # Get the singleton instance

    initial_year = GlobalState().get('initial_year') 

    # Set pandas to display all columns
    import pandas as pd
    # pd.set_option('display.max_columns', None)
    try:
        # Access the 'Revenue Growth' row and year `t` column (ensure t is a string)
        revenue_growth = model.Input.Assumptions['Revenue Growth'][t]
    except KeyError as e:
        print(f"Error accessing 'Revenue Growth' for year {t}: {e}")
        revenue_growth = 0 

    if t == initial_year:
        return model.Input.Balances['Revenue'][t]
    else:
        return Revenue(t-1) * (1 + revenue_growth)  # You can adjust the base revenue if needed

def COGS(t):
    """Cost of Goods Sold"""

    model = ModelSingleton.get_instance()  # Get the singleton instance
    cogs_revenue = model.Input.Assumptions['COGS/Revenues'][t]
    return Revenue(t) * cogs_revenue # Example constant cost of goods sold

def Operating_Expenses(t):
    """Operating Expenses"""
    return -30  # Example constant operating expense

def EBIT(t):
    """EBIT Earnings Before Interests and Taxes """
    return Revenue(t) + COGS(t) + Operating_Expenses(t)

def Depreciation(t):
    return -5

def Amortization(t):
    return -2

def EBITDA (t):
    """EBITDA Earnings Before Interests Taxes Depreciation and Amortization"""
    return Net_Income(t) - Interests(t) - Taxes(t, EBIT(t)) - Depreciation(t) - Amortization(t)

def EBITA (t):
    """EBITA Earnings Before Interest and Taxes """
    return Net_Income(t) - Interests(t) -  Taxes(t, EBIT(t)) - Amortization(t)

def Interests(t):
    return 0

def Net_Income(t):
    """Net income calculation (Revenue - COGS - Expenses - Interests - Taxes)"""
    return EBIT(t) - Interests(t) - Taxes(t, EBIT(t))

def NOPAT(t):
    """ NET OPERATING PROFIT AFTER TAXES"""
    return Net_Income(t) - Taxes(t, EBIT(t))

