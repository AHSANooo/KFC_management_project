from src.interfaces.customer_interface import CustomerInterface
from src.core.service_locator import ServiceLocator

def main():
    # Initialize service locator
    service_locator = ServiceLocator()

    # Directories for data files
    orders_dir = "config/orders/orders.json"
    products_dir = "config/products/products.json"
    inventory_dir = "config/inventory/inventory.json"

    # Create CustomerInterface instance
    customer_interface = CustomerInterface(orders_dir, products_dir, inventory_dir, service_locator)

    # Start the application
    customer_interface.start()


if __name__ == "__main__":
    main()
