from hash_table import ChainingHashTable
from package import Package
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

def main():
    package_hash_table = load_package_data()
    distance_data = load_distance_data()
    address_data = load_address_data()

if __name__ == "__main__":
    main()
