class Truck:
    def __init__(self):
        self.packages = []
        self.mileage = 0.0
        self.speed = 18
        self.max_capacity = 16

    def load_packages(self, packages):
        for package in packages:
            if len(self.packages) < self.max_capacity:
                self.packages.append(package)
            else:
                print(f"Truck is at max capacity. {package} not loaded.")
                break

    def get_num_packages(self):
        return len(self.packages)
    
    def get_packages(self):
        return self.packages
