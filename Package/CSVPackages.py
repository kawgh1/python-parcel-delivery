# import packages from CSV file
from Truck.Truck import Truck
from Package.Package import Package
import csv
from Util.HashTable import HashMap
from Location import LocationNode
from Location.LocationNode import LocationNode

# Create Truck Objects
truck_1 = Truck('truck_1')
truck_2 = Truck('truck_2')
global_distance = 0


# the times below represent the times that each truck leaves the hub
first_time = '8:00:00'
second_time = '09:10:00'
third_time = '10:20:00'

#  Read in package data from CSV file and create package objects with that data
#  Create key/value pair of package object and insert into HashTable
#  Sort packages according to special note or delivery time, etc. parameters
#  Space-time complexity is O(1)
with open('Data/Packages.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    truck_1_list = []
    truck_2_list = []
    leftovers = []
    holding = []

    # Create HashMap object to store key,value pairs
    HashMap1 = HashMap()

    # for row in readCSV:
    #     packageID_value = row[0]
    #     address_value = row[1]
    #     city = row[2]
    #     state = row[3]
    #     zip_code = row[4]
    #     delivery_time_value = row[5]
    #     weight_value = row[6]
    #     delivery_status = 'HUB'
    #     note_value = row[7]
    #     start_time = ''
    #     time_delivered = ''
    #     delivery_address_location = ''
    #
    #
    #  Space-time complexity is O(N)
    for row in readCSV:
        # package = (packageID_value=0, address_value=1, city=2, state=3, zip_code=4, delivery_time_value=5,
        # weight_value=6, delivery_status=X, note_value=7, start_time=X, time_delivered)
        package = Package(int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], 'HUB', row[7], '',
                          'not delivered')

        key = int(row[0])
        value = package

        # packages noted as only on truck 2 to truck 2
        if 'Can only be on truck 2' in package.note_value:
            truck_2_list.append(package)
        # delayed packages go out on truck_2 at 09:10:00
        if 'Delayed' in package.note_value:
            truck_2_list.append(package)
        # wrong addressed packages to be picked up later by truck_1 at 10:20:00
        if 'Wrong address' in package.note_value:
            package.address_value = '410 S State St'
            package.zip_value = '84111'
            leftovers.append(package)

        # items that have earlier delivery times and no other issues go on truck 1
        # the group packages (13, 14, 15, 16 and 20) have early delivery deadlines and thus go on truck 1
        if package.delivery_time_value != 'EOD' and 'Can only be on truck 2' not in package.note_value and 'Delayed' not in package.note_value and 'Wrong address' \
                not in package.note_value:
            truck_1_list.append(package)
        # Packages above must be delivered with 19, this ensures 19 is with the others above
        if '84115' in package.zip_code and 'EOD' in package.delivery_time_value and 'Delayed' not in package.note_value:
            truck_1_list.append(package)
        # group packages without early delivery times go to truck 2 to simplify sorting, none in this case
        if 'Must be delivered with' in package.note_value and 'EOD' in package.delivery_time_value:
            truck_2_list.append(package)
        # if a package was not assigned to a truck or to leftovers, it goes in 'holding'
        # until it can be reassigned below
        if package not in truck_1_list and package not in truck_2_list and package not in leftovers:
            holding.append(package)
        HashMap1.add(key, package)

    # fill trucks to max capacity where possible
    #  Space-time complexity is O(N)
    for package in holding:
        if len(truck_1_list) < 16:
            truck_1_list.append(package)

        elif len(truck_2_list) < 16:
            truck_2_list.append(package)
        else:
            leftovers.append(package)

    print('\n Truck 2 contains: \n')
    #  Space-time complexity is O(N)

    #  def update(self, key, value):
    for item in truck_2_list:

        item.start_time = first_time
        item.truck = 'truck_2'
        item.start_time = '09:10:00'
        print(item.packageID_value, item.address_value, item.delivery_time_value, item.note_value, item.truck)
    print('truck 2 length = ', len(truck_2_list))
    print('\n Truck 1 contains: \n')
    #  Space-time complexity is O(N)
    for item in truck_1_list:
        item.start_time = second_time
        item.truck = 'truck_1'
        item.start_time = '08:00:00'
        print(item.packageID_value, item.address_value, item.delivery_time_value, item.note_value, item.truck)
    print('truck 1 length = ', len(truck_1_list))
    print('\n Leftovers contains: \n')
    #  Space-time complexity is O(N)
    for item in leftovers:
        item.start_time = third_time
        item.truck = 'truck_1'
        print(item.packageID_value, item.address_value, item.delivery_time_value, item.note_value)
    print('leftovers length = ', len(leftovers))

    # print('\n Holding contains: \n')
    # for item in holding:
    #     print(item.packageID_value, item.address_value, item.delivery_time_value, item.note_value)
    # print('Holding length = ', len(holding))
##########################################################

# Once packages are sorted into correct lists, assign those lists to the truck objects
truck_1.package_list = truck_1_list
truck_2.package_list = truck_2_list

# Set Truck_2 start time to 09:10:00
truck_2.time = '9:10:00'
truck_2.time_list = ['9:10:00']

# print'truck_1.package_list = ', (truck_1.package_list)

# Check HashTable functionality
# print('HashMap \n', HashMap1.get(3))
# HashMap1.printHashMap()
# print(HashMap1.get(3))
# print(HashMap1.get('4'))
# print(HashMap1.get(10))


# Put distance values from DistanceData.CSV file into a list of distances
# will be used as a matrix of values to determine distances between locations
#  Space-time complexity is O(1)
with open('Data/DistanceData.csv') as csvfile:
    distanceCSV = csv.reader(csvfile, delimiter=',')
    distanceCSV = list(distanceCSV)
    # For developer use
    # print(distanceCSV)

# Put Locations and location info (address info, name, etc.) into a list of locations
#  Space-time complexity is O(1)
with open('Data/Locations.csv') as csvfile:
    locationsCSV = csv.reader(csvfile, delimiter=',')
    # For developer use
    locationsCSV = list(locationsCSV)
    # print(locationsCSV)

#   Create separate location lists for each Truck. This avoids Trucks mapping to the same
#   LocationNodes while in route, where LocationNodes may occur in both trucks, creating route conflicts
    locations_list_T1 = []
    locations_list_T2 = []

    #  Space-time complexity is O(N)
    for row in locationsCSV:
        # LocationNode(location_id, name, street_address)
        locationNode = LocationNode(int(row[0]), row[1], row[2])

        locations_list_T1.append(locationNode)
        locations_list_T2.append(locationNode)


# Print space for readability
print("\n\n\n")

# This get_truck_locations(truck) method assigns a list of LocationNodes to each truck
# based on the package addresses in the truck
# Space-time complexity is O(N^2)


def get_truck_locations(truck):

    truck_location_list = []

    if truck is truck_1:
        locations_list = locations_list_T1
    else:
        locations_list = locations_list_T2
    # Assign LocationNodes to each truck if a truck's package is addressed to that Location
    # Items in these truck_location_lists are used to determine next location on truck's route, unique to each truck
    # Space-time complexity is O(N^2)
    for packages in truck.package_list:
        for locations in locations_list:
            if packages.address_value == locations.address_value:

                locationNode = LocationNode(locations.location_id,
                                            locations.name + ' ' + truck.name + ' ', locations.address_value)
                truck.truck_location_list.append(locationNode)

                # remove chance to append duplicate LocationNodes of same location during for loop iteration
                # if multiple packages on truck have same address
                locations_list.remove(locations)

    print (' TRUCK ', truck.name, ' location list ')
    # Space-time complexity is O(N)
    for items in truck.truck_location_list:
        print (items.name)

    print ('\n\n\n')
    return truck_location_list


# This get_truck_locations(truck) method assigns a list of LocationNodes to each truck
# based on the package addresses in the truck
# Space-time complexity is O(N^2)
get_truck_locations(truck_1)
get_truck_locations(truck_2)

# create edges between LocationNodes in truck location list
# The edge 'weight' is the distance in miles between LocationNodes
# Space-time complexity is O(N^2)
truck_1.create_edges_for_truck_location_list()
truck_2.create_edges_for_truck_location_list()


# OPTIMIZE TRUCK LOCATION LIST AND DELIVER PACKAGES

# Prints Location lists, to ensure no duplicates
# i.e. truck visiting same node twice
#
# print('\n \n \n items in truck_1.locations_list \n ')
#
# for items in truck_1.truck_location_list:
#
#     print(items.name)
#
# print('\n \n \n items in truck_2.locations_list \n ')
#
# for items in truck_2.truck_location_list:
#
#     print(items.name)

# Used to check HashTable is still accurate
#print('Print HashMap1.get(2) = ', HashMap1.get(2))
#
#
#
#
# The '_____.optimize_truck_location_list' below both optimizes the route
#   and delivers the packages. Once this method is run and completed,
#   that truck's route is completed.
# 'global_distance' keeps track of total distance traveled by all trucks and routes
# Space-time complexity is O(N^2)
global_distance = truck_1.optimize_truck_location_list()
global_distance = global_distance + truck_2.optimize_truck_location_list()

# truck_1's first route finishes prior to 10:00:00,
# but a package in leftovers is not corrected until 10:20:00
# thus, truck_1 must 'wait' at the HUB to start its second route
# until the correction occurs
truck_1.time = '10:20:00'
truck_1.time_list = ['10:20:00']


# Once the first routes are completed, if any truck has a new route
# that truck's location_list must be reset and remapped
# Space-time complexity is O(1)
with open('Data/Locations.csv') as csvfile:
    locationsCSV = csv.reader(csvfile, delimiter=',')
    # For developer use
    # locationsCSV = list(locationsCSV)
    # print(locationsCSV)

    locations_list_T1 = []
    locations_list_T2 = []
    # Space-time complexity is O(N)
    for row in locationsCSV:
        # LocationNode(location_id, name, street_address)
        locationNode = LocationNode(int(row[0]), row[1], row[2])

        locations_list_T1.append(locationNode)
        locations_list_T2.append(locationNode)



# leftovers are the packages remaining at HUB to still be delivered
# Space-time complexity is O(1)
truck_1.package_list = leftovers


# This get_truck_locations(truck) method assigns a list of LocationNodes to each truck
# based on the package addresses in the truck
# Space-time complexity is O(N^2)
get_truck_locations(truck_1)


# Set adjaceniesList for each locationNode in the each truck's location_list
# this streamlines the process, setting adjacencies only for locations
# in same truck route (vs. all locations, including locations not in route)
#truck_1.set_truck_locationNodes_list()


# Create edges for graph of truck's location list
# Space-time complexity is O(N^2)
truck_1.create_edges_for_truck_location_list()

print('\n \n \n items in truck_1.locations_list FOR LEFTOVERS\n ')
# Space-time complexity is O(N)
for items in truck_1.truck_location_list:

    print(items.name)

# deliver leftover packages
# Space-time complexity is O(N^2)
global_distance = global_distance + truck_1.optimize_truck_location_list()

# Method used for other classes to access HashTable
# Space-time complexity is O(1)


def get_hash_map():
    return HashMap1
