import json
from datetime import datetime
from .file_saver import FileSaver
from .file_loader import FileLoader

class OrderManager:
    def __init__(self, orders_file, file_saver: FileSaver, file_loader: FileLoader):
        self.orders_file = orders_file
        self.file_saver = file_saver
        self.file_loader = file_loader
        self.load_orders()

    def load_orders(self):
        try:
            self.orders = self.file_loader.load(self.orders_file)
        except FileNotFoundError:
            self.orders = []

    def save_orders(self):
        self.file_saver.save(self.orders, self.orders_file)

    def place_order(self, customer_name, items, payment_method, total, total_discount, total_after_discount):
        order = {
            'customer_name': customer_name,
            'items': items,
            'payment_method': payment_method,
            'total': total,
            'total_discount': total_discount,
            'total_after_discount': total_after_discount,
            'datetime': datetime.now().isoformat()
        }
        self.orders.append(order)
        self.save_orders()
        return order
