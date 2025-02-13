# cashflow.py

def Operating_CashFlow(t):
    """Operating cash flows (e.g., Net Income + Depreciation)"""
    return 50  # Example constant value

def Investing_CashFlow(t):
    """Investing cash flows (e.g., purchase of fixed assets)"""
    return -30  # Example constant value

def Financing_CashFlow(t):
    """Financing cash flows (e.g., loans taken, dividends paid)"""
    return 20  # Example constant value

def Net_CashFlow(t):
    """Net cash flow calculated as the sum of operating, investing, and financing activities"""
    return Operating_CashFlow(t) + Investing_CashFlow(t) + Financing_CashFlow(t)
