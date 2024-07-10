import json
import csv

class DataAdapter:
    def __init__(self, adapter_type):
        self.adapter_type = adapter_type
        self.connection = None  # Placeholder for connection object if needed

    def connect(self):
        # Implement connection logic if required for specific adapters
        if self.adapter_type == 'json':
            # Example: Open connection to a JSON database or service
            self.connection = None  # Replace with actual connection logic
        elif self.adapter_type == 'csv':
            # Example: Open connection to a CSV file or database
            self.connection = None  # Replace with actual connection logic
        else:
            raise ValueError(f"Unsupported adapter type: {self.adapter_type}")

    def load(self, file_path):
        try:
            if not self.connection:
                self.connect()  # Connect if not already connected

            if self.adapter_type == 'json':
                return self.load_json(file_path)
            elif self.adapter_type == 'csv':
                return self.load_csv(file_path)
            else:
                raise ValueError(f"Unsupported adapter type: {self.adapter_type}")
        finally:
            self.disconnect()  # Ensure disconnection after loading

    def disconnect(self):
        # Implement disconnection logic if required for specific adapters
        if self.connection:
            # Example: Close connection to JSON or CSV source
            self.connection = None  # Replace with actual disconnection logic

    def save_data(self, data, file_path):
        if self.adapter_type == 'json':
            self.save_json(data, file_path)
        elif self.adapter_type == 'csv':
            self.save_csv(data, file_path)
        else:
            raise ValueError(f"Unsupported adapter type: {self.adapter_type}")

    def load_json(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def save_json(self, data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def load_csv(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def save_csv(self, data, file_path):
        with open(file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

