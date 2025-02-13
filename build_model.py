# build_model.py
import os
import modelx as mx
import pnl
import balance_sheet
import cashflow

def build():
    """Build a model and return it.

    Create spaces for pnl, Balance Sheet, and Cash Flow and project them.
    """

    # Ensure the current directory is correct
    os.chdir(os.path.abspath(os.path.dirname(__file__)))

    # Create a new model
    model = mx.new_model(name='Financial_Statements_Model')

    # ------------------------------------------------------------------------
    # Build P&L space
    pnl_space = model.new_space(
        name='pnl',
        formula=lambda: {'Revenue': pnl.Revenue, 'COGS': pnl.COGS, 'Operating_Expenses': pnl.Operating_Expenses,
                         'Net_Income': pnl.Net_Income}
    )

    # ------------------------------------------------------------------------
    # Build Balance Sheet space
    balance_sheet_space = model.new_space(
        name='BalanceSheet',
        formula=lambda: {'Current_Assets': balance_sheet.Current_Assets, 'Non_Current_Assets': balance_sheet.Non_Current_Assets,
                         'Current_Liabilities': balance_sheet.Current_Liabilities, 'Long_Term_Liabilities': balance_sheet.Long_Term_Liabilities,
                         'Equity': balance_sheet.Equity}
    )

    # ------------------------------------------------------------------------
    # Build Cash Flow space
    cashflow_space = model.new_space(
        name='CashFlow',
        formula=lambda: {'Operating_CashFlow': cashflow.Operating_CashFlow, 'Investing_CashFlow': cashflow.Investing_CashFlow,
                         'Financing_CashFlow': cashflow.Financing_CashFlow, 'Net_CashFlow': cashflow.Net_CashFlow}
    )

    # ------------------------------------------------------------------------
    # Build Projection space (combines all previous spaces)
    proj_refs = {
        'pnl': pnl_space,
        'BalanceSheet': balance_sheet_space,
        'CashFlow': cashflow_space
    }

    def proj_params():
        return {
            'pnl': proj_refs['pnl'],
            'BalanceSheet': proj_refs['BalanceSheet'],
            'CashFlow': proj_refs['CashFlow']
        }

    projection = model.new_space(
        name='Projection',
        formula=proj_params,
        refs=proj_refs
    )

    # ------------------------------------------------------------------------
    # Add cells dynamically to the model's 'cells' attribute with standardized names
    model.cells = {
        'Revenue': pnl.Revenue,
        'COGS': pnl.COGS,
        'Operating_Expenses': pnl.Operating_Expenses,
        'Net_Income': pnl.Net_Income,
        'Current_Assets': balance_sheet.Current_Assets,
        'Non_Current_Assets': balance_sheet.Non_Current_Assets,
        'Current_Liabilities': balance_sheet.Current_Liabilities,
        'Long_Term_Liabilities': balance_sheet.Long_Term_Liabilities,
        'Equity': balance_sheet.Equity,
        'Operating_CashFlow': cashflow.Operating_CashFlow,
        'Investing_CashFlow': cashflow.Investing_CashFlow,
        'Financing_CashFlow': cashflow.Financing_CashFlow,
        'Net_CashFlow': cashflow.Net_CashFlow
    }

    return model

