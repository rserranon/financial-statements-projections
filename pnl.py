# pnl.py

def Taxes(t, net_income):
    """Taxes based on net income"""
    return 0.2 * net_income  # 20% tax

def Revenue(t):
    """Revenue or Sales"""
    return 100  # Example constant revenue

def COGS(t):
    """Cost of Goods Sold"""
    return 50  # Example constant cost of goods sold

def Operating_Expenses(t):
    """Operating Expenses"""
    return 30  # Example constant operating expense

def EBIT(t):
    """EBIT Earnings Before Interests and Taxes """
    return Revenue(t) - COGS(t) - Operating_Expenses(t)

def Depreciation(t):
    return 0

def Amortization(t):
    return 0

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

