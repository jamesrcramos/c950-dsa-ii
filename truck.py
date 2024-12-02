import datetime

class Truck:
    def __init__(self):
        self.packages = []
        self.mileage = 0.0
        self.speed = 18
        self.max_capacity = 16
        self.current_address = "4001 South 700 East"
        self.current_time = datetime.timedelta(hours=8)

    def get_num_packages(self):
        return len(self.packages)
    
    def get_current_address(self):
        return self.current_address
    
    def get_packages(self):
        return self.packages
    
    def get_mileage(self):
        return self.mileage
    
    def set_current_time(self, time):
        self.current_time = time
    
    def set_current_address(self, address):
        self.current_address = address

    def load_packages(self, packages):
        for package in packages:
            if len(self.packages) < self.max_capacity:
                self.packages.append(package)
            else:
                print(f"Truck is at max capacity. {package} not loaded.")
                break

    def add_mileage(self, distance):
        self.mileage += distance
