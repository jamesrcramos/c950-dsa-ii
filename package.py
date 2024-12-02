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
        self.delivery_status = "At Hub"
        self.delivery_time = None

    def get_address(self):
        return self.address
    
    def set_delivery_status(self, status):
        self.delivery_status = status
