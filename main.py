from hash_table import ChainingHashTable
from package import Package
from truck import Truck
import csv

def load_package_data():
    hash_table = ChainingHashTable()
    with open('data/packages.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        
        for data in csv_reader:
            package = Package()
            package.id = int(data[0])
            package.address = data[1]
            package.city = data[2]
            package.state = data[3] 
            package.zip = data[4]
            package.delivery_deadline = data[5]
            package.weight = float(data[6])
            package.special_notes = data[7] if data[7] else None
            
            hash_table.insert(package.id, package)
    return hash_table

def load_distance_data():
    distance_data = []
    with open('data/distances.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Filter out empty strings and convert to float
            filtered_row = [float(dist) if dist else 0.0 for dist in row]
            distance_data.append(filtered_row)
    return distance_data

def load_address_data():
    address_data = []
    with open('data/addresses.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Extract just the address part (before the zip code in parentheses)
            address = row[0].split('\n')[0].strip()
            address_data.append(address)
    return address_data

def load_trucks(truck1, truck2, truck3, package_hash_table):
    early_delivery_packages = [
        package_hash_table.search(1), package_hash_table.search(13),
        package_hash_table.search(14), package_hash_table.search(15),
        package_hash_table.search(16), package_hash_table.search(20),
        package_hash_table.search(29), package_hash_table.search(30),
        package_hash_table.search(31), package_hash_table.search(34),
        package_hash_table.search(37), package_hash_table.search(40)
    ]
    delayed_packages = [
        package_hash_table.search(3), package_hash_table.search(6),
        package_hash_table.search(18), package_hash_table.search(25),
        package_hash_table.search(28), package_hash_table.search(32),
        package_hash_table.search(36), package_hash_table.search(38)
    ]
    wrong_address_packages = [
        package_hash_table.search(9)
    ]
    other_packages = [
        package_hash_table.search(2), package_hash_table.search(4),
        package_hash_table.search(5), package_hash_table.search(7),
        package_hash_table.search(8), package_hash_table.search(10),
        package_hash_table.search(11), package_hash_table.search(12),
        package_hash_table.search(17), package_hash_table.search(19),
        package_hash_table.search(21), package_hash_table.search(22),
        package_hash_table.search(23), package_hash_table.search(24),
        package_hash_table.search(26), package_hash_table.search(27),
        package_hash_table.search(33), package_hash_table.search(35),
        package_hash_table.search(39)
    ]

    truck1.load_packages(early_delivery_packages)
    truck2.load_packages(delayed_packages)
    truck3.load_packages(wrong_address_packages)
    for package in other_packages:
        if truck3.get_num_packages() < 16:
            truck3.load_packages([package])
        else:
            print(f"Truck 3 is at max capacity. {package.id} not loaded.")
            break
    # Load remaining packages into truck 1 as it will be available first
    for package in other_packages:
        if package not in truck3.get_packages():
            if truck1.get_num_packages() < 16:
                truck1.load_packages([package])
            else:
                print(f"Truck 1 is at max capacity. {package.id} not loaded.")
                break

def get_address_index(address, address_data):
    """Find the index of an address in the address data list"""
    try:
        return address_data.index(address)
    except ValueError:
        print(f"Address not found: {address}")
        return -1

def deliver_packages(truck, package_hash_table, address_data, distance_data):
    packages = truck.get_packages()

    # take current address from truck
    # find closest address from current address and all undelivered packages
    
    # update truck's current address to the closest address
    # update truck's mileage to the distance between the current address and the closest address

def main():
    package_hash_table = load_package_data()
    distance_data = load_distance_data()
    address_data = load_address_data()

    truck1 = Truck()  # Early delivery + remaining no constraints
    truck2 = Truck()  # Delayed + can only be loaded on truck 2 + wrong address
    truck3 = Truck()  # No constraints
    load_trucks(truck1, truck2, truck3, package_hash_table)
    deliver_packages(truck1, package_hash_table, address_data, distance_data)
    deliver_packages(truck2, package_hash_table, address_data, distance_data)
    # deliver_packages(truck3, package_hash_table, address_data, distance_data)

if __name__ == "__main__":
    main()
