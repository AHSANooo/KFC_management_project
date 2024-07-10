import json
#from src.core.file_loader import FileLoader
from src.core.file_saver import FileSaver

class JSONLoader():
    def connect(self):
        pass  # No connection needed for JSON files

    def load(self, file_path: str) -> dict:
        with open(file_path, 'r') as file:
            return json.load(file)

    def disconnect(self):
        pass  # No disconnection needed for JSON files

class JSONSaver(FileSaver):
    def connect(self):
        pass  # No connection needed for JSON files

    def save(self, data: dict, file_path: str):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def disconnect(self):
        pass  # No disconnection needed for JSON files
