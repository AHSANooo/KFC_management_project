from .file_loader import FileLoader
from .file_saver import FileSaver
from .adapters import DataAdapter

class ProductManager:
    def __init__(self, products_file, file_loader: FileLoader, file_saver: FileSaver, data_adapter: DataAdapter):
        self.products_file = products_file
        self.file_loader = file_loader
        self.file_saver = file_saver
        self.data_adapter = data_adapter
        self.load_products()

    def load_products(self):
        try:
            self.products = self.file_loader.load(self.products_file)
        except FileNotFoundError:
            self.products = {}

    def save_products(self):
        self.file_saver.save(self.products, self.products_file)

    def update_products(self, updated_products):
        self.products = updated_products
        self.save_products()

    def get_products(self):
        return self.products

    def get_products_data(self):
        return self.data_adapter.load_data(self.products_file)

    def save_products_data(self, data):
        self.data_adapter.save_data(data, self.products_file)
