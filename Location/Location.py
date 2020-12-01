import sys


class Location(object):

    def __init__(self, location_id, name, street_address, city, state, zip_code):

        self.location_id = location_id
        self.name = name
        self.street_address = street_address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.visited = False
        self.predecessor = None
        self.adjacenciesList = []
        self.minDistance = sys.maxsize
