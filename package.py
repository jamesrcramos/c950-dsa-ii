class Package:
    def __init__(self):
        self.id = None
        self.address = None
        self.city = None
        self.state = None
        self.zip = None
        self.delivery_deadline = None
        self.weight = None
        self.special_notes = None
        self.departure_time = None
        self.truck = None;
        self.delivery_status = "At Hub"
        self.delivery_time = None

    def get_address(self):
        return self.address
    
    def get_departure_time(self):
        return self.departure_time
    
    def get_delivery_time(self):
        return self.delivery_time
    
    def set_departure_time(self, time):
        self.departure_time = time

    def set_truck(self, truck_number):
        self.truck = truck_number
    
    def set_delivery_status(self, status):
        self.delivery_status = status

    def set_delivery_time(self, time):
        self.delivery_time = time

