from hash_table import ChainingHashTable
from package import Package
import csv

def main():
    hash_table = ChainingHashTable()
    
    # Read and parse the packages CSV file
    with open('data/packages.csv', 'r') as file:
        csv_reader = csv.reader(file)
        
        # Skip header row
        next(csv_reader)
        
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
            
            # Insert package into hash table using ID as key
            hash_table.insert(package.id, package)

    distance_data = []
    with open('data/distances.csv', 'r') as file:
        csv_reader = csv.reader(file)
            
        for row in csv_reader:
            # Filter out empty strings and convert to float
            filtered_row = [float(dist) if dist else 0.0 for dist in row]
            distance_data.append(filtered_row)


if __name__ == "__main__":
    main()
