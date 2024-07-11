import os
from src.interfaces.customer_interface import CustomerInterface
from src.core.service_locator import ServiceLocator

def list_files_in_directory(directory_path):
    try:
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        if not files:
            raise FileNotFoundError(f"No files found in directory: {directory_path}")
        return files
    except Exception as e:
        raise FileNotFoundError(str(e))

def main():
    # Initialize service locator
    service_locator = ServiceLocator()

    # Directories for data files
    orders_dir_path = "config/orders/"
    products_dir_path = "config/products/"
    inventory_dir_path = "config/inventory/"

    # Get the first files in each directory
    orders_file = os.path.join(orders_dir_path, list_files_in_directory(orders_dir_path)[0])
    products_file = os.path.join(products_dir_path, list_files_in_directory(products_dir_path)[0])
    inventory_file = os.path.join(inventory_dir_path, list_files_in_directory(inventory_dir_path)[0])

    # Create CustomerInterface instance
    customer_interface = CustomerInterface(orders_file, products_file, inventory_file, service_locator)

    # Start the application
    customer_interface.start()


if __name__ == "__main__":
    main()
