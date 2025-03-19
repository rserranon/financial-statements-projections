# pnl.py
from model_singleton import ModelSingleton
from global_state import GlobalState
from utils import get_assumption_value  # Import the helper function

model = ModelSingleton.get_instance()  # Get the singleton instance

def Revenue(t):
    """Revenue or Sales"""

    initial_year = GlobalState().get('initial_year')
    
    if t == initial_year:
        return model.Input.Balances['Revenue'][t]
    else:
        revenue_growth = get_assumption_value(model, 'Revenue Growth', t)
        return Revenue(t-1) * (1 + revenue_growth)  # Adjust the base revenue if needed

def COGS(t):
    """Cost of Goods Sold"""

    cogs_revenue = get_assumption_value(model, 'COGS/Revenues', t)
    return Revenue(t) * cogs_revenue * (-1)  # COGS are negative balances

def SGA(t):
    """Operating Expenses"""
    
    sga = get_assumption_value(model, 'SG&A/Revenues', t)
    return Revenue(t) * sga * (-1)  # SG&A are negative balances

def EBIT(t):
    """EBIT Earnings Before Interests and Taxes"""
    return Revenue(t) + COGS(t) + SGA(t)

def Depreciation(t):
    """Depreciation (assuming it's an assumption now, else it defaults to -5)"""
    return get_assumption_value(model, 'Depreciation', t, -5)

def Amortization(t):
    """Amortization (assuming it's an assumption now, else it defaults to -2)"""
    return get_assumption_value(model, 'Amortization', t, -2)

def EBITDA(t):
    """EBITDA Earnings Before Interests Taxes Depreciation and Amortization"""
    return EBIT(t) + Depreciation(t) + Amortization(t)

def EBITA(t):
    """EBITA Earnings Before Interest and Taxes"""
    return EBIT(t) + Amortization(t)

def Interests(t):
    """Interest Expense"""
    return 0  # Assuming 0 as a placeholder for interest expense

def Taxes(t):
    """Taxes based on net income"""

    marginal_tax_rate = get_assumption_value(model, 'Tax Rate', t)
    return EBIT(t) * marginal_tax_rate * (-1)  # Taxes are negative balances

def Net_Income(t):
    """Net income calculation (Revenue - COGS - Expenses - Interests - Taxes)"""
    return EBIT(t) - Interests(t) - Taxes(t)

def NOPAT(t):
    """NET OPERATING PROFIT AFTER TAXES"""
    return EBITA(t) + Taxes(t)
