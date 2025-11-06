class Car:
    url_photo = None
    name = None
    price = None
    engine = None
    transmission = None
    drive = None
    body_type = None
    color = None
    mileage = None
    wheel = None
    url = None
    
    def __init__(self, url_photo = None, name = None, price = None, engine = None, transmission = None, drive = None, body_type = None, color = None, mileage = None, wheel = None, url = None):
        self.url_photo = url_photo
        self.name = name
        self.price = price
        self.engine = engine
        self.transmission = transmission
        self.drive = drive
        self.body_type = body_type
        self.color = color
        self.mileage = mileage
        self.wheel = wheel
        self.url = url
        
    def print(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")