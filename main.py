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

def load_trucks():
    truck1 = Truck()  # Early delivery
    truck2 = Truck()  # Delayed + can only be loaded on truck 2 + wrong address
    truck3 = Truck()  # No constraints

    early_delivery_packages = [
        1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40
    ]
    delayed_packages = [
        3, 6, 18, 25, 28, 32, 36, 38
    ]
    wrong_address_packages = [
        9
    ]   
    other_packages = [
        2, 4, 5, 7, 8, 10, 11, 12, 17, 19, 21, 22, 23,
        24, 26, 27, 33, 35, 39
    ]

    truck1.load_packages(early_delivery_packages)
    truck2.load_packages(delayed_packages)
    truck3.load_packages(wrong_address_packages)
    for package in other_packages:
        if truck3.get_num_packages() < 16:
            truck3.load_packages([package])
        else:
            print(f"Truck 3 is at max capacity. {package} not loaded.")
            break
    # Load remaining packages into truck 1 as it will be available first
    for package in other_packages:
        if package not in truck3.get_packages():
            if truck1.get_num_packages() < 16:
                truck1.load_packages([package])
            else:
                print(f"Truck 1 is at max capacity. {package} not loaded.")
                break
                    
    return truck1, truck2, truck3

def main():
    package_hash_table = load_package_data()
    distance_data = load_distance_data()
    address_data = load_address_data()

    truck1, truck2, truck3 = load_trucks()

if __name__ == "__main__":
    main()
