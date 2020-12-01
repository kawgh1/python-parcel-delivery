import sys


class LocationNode(object):

    def __init__(self, location_id, name, address_value):

        self.location_id = location_id
        self.name = name
        self.address_value = address_value
        self.visited = False
        self.predecessor = None
        self.adjacenciesList = []
        self.minDistance = sys.maxsize
