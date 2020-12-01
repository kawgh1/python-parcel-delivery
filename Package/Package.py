class Package(object):

    def __init__(self, packageID_value, address_value, city, state, zip_code, delivery_time_value, weight_value,
                 delivery_status, note_value, start_time, time_delivered):
        self.packageID_value = packageID_value
        self.address_value = address_value
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_time_value = delivery_time_value
        self.weight_value = weight_value
        self.note_value = note_value
        self.delivery_status = delivery_status
        self.delivery_address_location_id = 0
        self.start_time = start_time
        self.time_delivered = time_delivered

        # Notes on import from CSV Packages file
        #
        # packageID_value = row[0]
        # address_value = row[1]
        # city_value = row[2]
        # state_value = row[3]
        # zip_value = row[4]
        # delivery_time_value = row[5]
        # weight_value = row[6]
        # note_value = row[7]
        # delivery_start_time = ''
        # delivery_address_location = ''
        # delivery_status = 'HUB'