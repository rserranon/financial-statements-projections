# utils.py
def get_assumption_value(model, category, t, default_value=0):
    """Helper function to get assumption values with error handling"""
    try:
        # Access the assumption value for category and year `t`
        return model.Input.Assumptions[category][t]
    except KeyError as e:
        print(f"Error accessing '{category}' for year {t}: {e}")
        return default_value
