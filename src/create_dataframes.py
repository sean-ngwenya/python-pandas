import pandas as pd
import numpy as np


def create_from_dict():
    data = {
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "age": [25, 30, 35, 28, 32],
        "city": ["Harare", "Bulawayo", "Harare", "Gweru", "Bulawayo"],
        "salary": [50000, 60000, 75000, 55000, 70000],
    }
    return pd.DataFrame(data)


def create_from_numpy():
    arr = np.random.randint(0, 100, (5, 3))
    return pd.DataFrame(arr, columns=["A", "B", "C"])
