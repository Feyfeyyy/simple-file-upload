from .csv_parser import CSVParser
from .json_parser import JSONParser


def get_constructor(file_name):
    if file_name.endswith(".csv"):
        return CSVParser()
    elif file_name.endswith(".json"):
        return JSONParser()
    else:
        raise ValueError("Unsupported file type")
