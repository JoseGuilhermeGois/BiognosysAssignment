import pandas as pd
from pandas import DataFrame


FILE_PATH = "data/20240625_113525_BGS_Factory_Report.parquet"


def read_file_path() -> DataFrame:
    """Function to read the file using the read_parquet function and fastparquet engine."""
    data = pd.read_parquet(path=FILE_PATH, engine="fastparquet")

    if data.empty:
        raise ValueError("No data available in the file path provided")
    
    return data
