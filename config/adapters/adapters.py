from .json_adapter import JSONDataAdapter
from .csv_adapter import CSVDataAdapter
import os

class DataAdapterFactory:
    @staticmethod
    def get_adapter(file_path):
        _, ext = os.path.splitext(file_path)
        if ext == '.json':
            return JSONDataAdapter(file_path)
        elif ext == '.csv':
            return CSVDataAdapter(file_path)
        else:
            raise ValueError("Unsupported file format")
