from typing import Dict
from ..core.file_loader import FileLoader
from ..core.file_saver import FileSaver
from ..core.service_locator import ServiceLocator

class InventoryManager:
    def __init__(self, inventory_file: str, service_locator: ServiceLocator):
        self.inventory_file = inventory_file
        self.data_adapter = service_locator.get_data_adapter(self.inventory_file)
        self.file_loader = FileLoader(self.data_adapter)
        self.file_saver = FileSaver(self.data_adapter)
        self.inventory = self.load_inventory()

    def load_inventory(self) -> Dict[str, int]:
        try:
            inventory = self.file_loader.load()
            return inventory
        except Exception as e:
            print(f"Error loading inventory: {e}")
            return {}

    def save_inventory(self, inventory: Dict[str, int]):
        try:
            self.file_saver.save(inventory)
        except Exception as e:
            print(f"Error saving inventory: {e}")

    def update_inventory(self, product_id: str, quantity: int):
        if product_id in self.inventory:
            self.inventory[product_id] += quantity
        else:
            self.inventory[product_id] = quantity
        self.save_inventory(self.inventory)

    def check_availability(self, product_id: str, quantity: int) -> bool:
        if product_id in self.inventory and self.inventory[product_id] >= quantity:
            return True
        return False

    def decrease_inventory(self, product_id: str, quantity: int):
        if product_id in self.inventory and self.inventory[product_id] >= quantity:
            self.inventory[product_id] -= quantity
            self.save_inventory(self.inventory)
        else:
            raise ValueError("Insufficient quantity in inventory")
