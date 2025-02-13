# load_assumptions.py
import modelx as mx
import pandas as pd

def load_assumptions(model, input_file):
    """Load assumptions into the model's Input space from an Excel file."""
    inp = model.new_space(name='Input')
    inp.allow_none = True

    # Load the assumptions data from Excel using pandas
    assumptions_df = pd.read_excel(input_file, sheet_name='Assumptions', index_col=0)
    startin_balances_df = pd.read_excel(input_file, sheet_name='Balances', index_col=0)
 

    # If you want to transpose the data (assuming years are in columns and assumptions in rows)
    assumptions_df = assumptions_df.transpose()
    startin_balances_df = startin_balances_df.transpose()

    # Load the data into the model using new_pandas
    inp.new_pandas(name="Assumptions", path=input_file, data=assumptions_df, file_type="excel", sheet="Assumptions")
    inp.new_pandas(name="Balances", path=input_file, data=startin_balances_df, file_type="excel", sheet="Balances")

    return inp
