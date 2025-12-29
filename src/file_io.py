def save_to_csv(df, path):
    df.to_csv(path, index=False)


def load_from_csv(path):
    import pandas as pd

    return pd.read_csv(path)
