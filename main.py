from hash_table import ChainingHashTable
from package import Package
from truck import Truck
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

    # print(hash_table.table)
    print("\nPackage Details:")
    for i in range(1, 41):
        package = hash_table.search(i)
        print(f"\nPackage {package.id}:")
        print(f"Address: {package.address}")
        print(f"City: {package.city}")
        print(f"State: {package.state}")
        print(f"ZIP: {package.zip}")
        print(f"Delivery Deadline: {package.delivery_deadline}")
        print(f"Weight: {package.weight}")
        print(f"Special Notes: {package.special_notes}")
        print(f"Delivery Status: {package.delivery_status}")
        print(f"Delivery Time: {package.delivery_time}")


    # Load trucks
    truck1 = Truck() # Early delivery
    truck2 = Truck() # Delayed + can only be loaded on truck 2
    truck3 = Truck() # Wrong address + remaining

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


if __name__ == "__main__":
    main()
