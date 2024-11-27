from hash_table import ChainingHashTable
from package import Package

def main():
    hash_table = ChainingHashTable()
    
    # Read and parse the packages CSV file
    with open('data/packages.csv', 'r') as file:
        # Skip header row
        next(file)
        
        for line in file:
            # Split the line and clean up whitespace
            data = [field.strip() for field in line.strip().split(',')]
            
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


if __name__ == "__main__":
    main()
