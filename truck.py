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
                print("Truck is at max capacity")
                break
