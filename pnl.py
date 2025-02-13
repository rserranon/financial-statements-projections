# pnl.py

def Revenue(t):
    """Revenue or Sales"""
    return 100  # Example constant revenue

def COGS(t):
    """Cost of Goods Sold"""
    return 50  # Example constant cost of goods sold

def Operating_Expenses(t):
    """Operating Expenses"""
    return 30  # Example constant operating expense

def Taxes(t, net_income):
    """Taxes based on net income"""
    return 0.2 * net_income  # 20% tax

def Net_Income(t):
    """Net income calculation (Revenue - COGS - Expenses - Taxes)"""
    return Revenue(t) - COGS(t) - Operating_Expenses(t) - Taxes(t, Revenue(t) - COGS(t) - Operating_Expenses(t))
