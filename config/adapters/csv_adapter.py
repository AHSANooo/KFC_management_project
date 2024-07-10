import csv

class CSVDataAdapter:
    def __init__(self, file_path):
        self.file_path = file_path

    def connect(self):
        pass  # Connection setup if required

    def load(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def save(self, data):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    def disconnect(self):
        pass  # Cleanup if required
