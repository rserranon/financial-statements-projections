# pnl.py
from model_singleton import ModelSingleton
from global_state import GlobalState


model = ModelSingleton.get_instance()  # Get the singleton instance


def Revenue(t):
    """Revenue or Sales"""

    initial_year = GlobalState().get('initial_year') 
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

    cogs_revenue = model.Input.Assumptions['COGS/Revenues'][t]
    return Revenue(t) * cogs_revenue * (-1) # COGS are negative balances

def SGA(t):
    """Operating Expenses"""
    sga = model.Input.Assumptions['SG&A/Revenues'][t]
    return Revenue(t) * sga * (-1) # SG&A are negative balances


def EBIT(t):
    """EBIT Earnings Before Interests and Taxes """
    return Revenue(t) + COGS(t) + SGA(t)

def Depreciation(t):
    return -5

def Amortization(t):
    return -2

def EBITDA (t):
    """EBITDA Earnings Before Interests Taxes Depreciation and Amortization"""
    return Net_Income(t) - Interests(t) - Taxes(t) - Depreciation(t) - Amortization(t)

def EBITA (t):
    """EBITA Earnings Before Interest and Taxes """
    return Net_Income(t) - Interests(t) -  Taxes(t) - Amortization(t)

def Interests(t):
    return 0

def Taxes(t):
    """Taxes based on net income"""

    marginal_tax_rate = model.Input.Assumptions['Tax Rate'][t]
    return EBIT(t) * marginal_tax_rate * (-1) # Taxes are negative balances

def Net_Income(t):
    """Net income calculation (Revenue - COGS - Expenses - Interests - Taxes)"""
    return EBIT(t) - Interests(t) - Taxes(t)

def NOPAT(t):
    """ NET OPERATING PROFIT AFTER TAXES"""
    return EBITA(t) + Taxes(t)

