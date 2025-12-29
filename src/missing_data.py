import pandas as pd
import numpy as np


def create_missing_data():
    data = {
        "A": [1, 2, np.nan, 4, 5],
        "B": [5, np.nan, np.nan, 8, 9],
        "C": [10, 11, 12, 13, 14],
    }
    return pd.DataFrame(data)


def handle_missing(df):
    return {
        "dropped": df.dropna(),
        "filled_zero": df.fillna(0),
        "filled_mean": df.fillna(df.mean()),
    }
