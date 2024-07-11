import csv

class CSVDataAdapter:
    def __init__(self, file_path):
        self.file_path = file_path

    def connect(self):
        pass  # Connection setup if required

    def load(self):
        inventory = {}
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:  # Ensure there are exactly two columns per row
                    item, quantity = row
                    inventory[item] = int(quantity)
        return inventory

    def save(self, data):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            for item, quantity in data.items():
                writer.writerow([item, quantity])

    def disconnect(self):
        pass  # Cleanup if required

    def load_order(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def save_order(self, data):
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)