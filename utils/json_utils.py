from flask import json
from pandas import DataFrame


def convert_to_json_format(data_result: DataFrame) -> json:
    """Function to convert the dataframe to json format."""
    return data_result.to_dict(orient='records')
