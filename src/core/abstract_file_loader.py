from abc import ABC, abstractmethod
from typing import Any

class AbstractFileLoader(ABC):
    """
    Abstract base class for file loaders.
    Defines the interface for loading JSON and CSV files.
    """

    @abstractmethod
    def load_json(self, file_name: str) -> Any:
        """
        Load JSON data from a file.

        Args:
            file_name (str): Name of the JSON file to load.

        Returns:
            Any: Loaded data from the JSON file.
        """
        pass

    @abstractmethod
    def load_csv(self, file_name: str) -> Any:
        """
        Load CSV data from a file.

        Args:
            file_name (str): Name of the CSV file to load.

        Returns:
            Any: Loaded data from the CSV file.
        """
        pass
