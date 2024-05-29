import pandas as pd

def read_csv(file_path) -> pd.DataFrame:
    """
    Read a CSV file and return a pandas DataFrame.
    """
    return pd.read_csv(file_path)
