# balance_sheet.py
from model_singleton import ModelSingleton
from global_state import GlobalState
from pnl import Net_Income
from utils import get_assumption_value

model = ModelSingleton.get_instance()  # Get the singleton instance
initial_year = GlobalState().get('initial_year') 


def Beggining_Retained_Earnings(t):
    """Calculate Retained Earnings"""

    if t == initial_year:
        return  0
    else:
        return Beggining_Retained_Earnings(t-1) # Initial balace = last period Beggining_Retained_Earnings 

def Common_Dividends(t):
    """Calculate common and alternative preferred dividends"""
    return 0

def Retained_Earnings(t):
    """"Return the Retained Earnings after paying dividends and adjustments"""
    return Beggining_Retained_Earnings(t) + Net_Income(t) + Common_Dividends(t)
