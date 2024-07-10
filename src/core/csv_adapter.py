import csv
#from src.core.file_loader import FileLoader
from src.core.file_saver import FileSaver

class CSVLoader():
    def connect(self):
        pass  # No connection needed for CSV files

    def load(self, file_path: str) -> list:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def disconnect(self):
        pass  # No disconnection needed for CSV files

class CSVSaver(FileSaver):
    def connect(self):
        pass  # No connection needed for CSV files

    def save(self, data: list, file_path: str):
        with open(file_path, 'w', newline='') as file:
            if data:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)

    def disconnect(self):
        pass  # No disconnection needed for CSV files
