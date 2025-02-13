# balance_sheet.py

def Current_Assets(t):
    """Current assets"""
    return 80  # Example constant value

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
