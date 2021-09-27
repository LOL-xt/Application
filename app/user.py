from .database import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    ip = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Numeric, nullable=True)
    longitude = db.Column(db.Numeric, nullable=True)
    country = db.Column(db.String, nullable=True)
    city = db.Column(db.String, nullable=True)

    def __init__(self, ip, name):
        self.ip = ip
        self.name = name
        self.latitude = None
        self.longitude = None
        self.country = None
        self.city = None

    def get_ip(self):
        return self.ip

    def set_ip(self, new_ip):
        self.ip = new_ip

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_latitude(self):
        return self.latitude

    def set_latitude(self, new_latitude):
        self.latitude = new_latitude

    def get_longitude(self):
        return self.longitude

    def set_longitude(self, new_longitude):
        self.longitude = new_longitude

    def get_country(self):
        return self.country

    def set_country(self, new_country):
        self.country = new_country

    def get_city(self):
        return self.city

    def set_city(self, new_city):
        self.city = new_city

    def serialize(self):
        return {
            'id': self.id,
            'ip': self.ip,
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'country': self.country,
            'city': self.city
        }
