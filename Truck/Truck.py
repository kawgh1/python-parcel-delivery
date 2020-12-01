from Util.DistanceChecker import distanceCSV
from Util.DistanceChecker import current_distance
from Location.Edge import Edge
from Location.LocationNode import LocationNode
import datetime


class Truck(object):
    def __init__(self, name):

        self.name = name
        self.package_list = []
        self.time = '8:00:00'
        self.distance_traveled = float(0) # distance traveled
        self.truck_location_list = []
        self.truck_optimized_location_list = []
        self.truck_edge_list = []
        self.time_list = ['8:00:00']

    def print_truck_package_list(self):

        print(self, '.package_list = ', self.package_list)

        for items in self.package_list:
            print (items.address_value, 'package ID = ', items.packageID_value)

    # create edges between LocationNodes in truck location list
    # The edge 'weight' is the distance in miles between LocationNodes
    # Space-time complexity is O(N^2)
    def create_edges_for_truck_location_list(self):

        # Add 'HUB' to truck_location_list to be starting LocationNode
        # Space-time complexity is O(1)
        HUB = LocationNode(int(0), 'HUB', '4001 South 700 East')
        self.truck_location_list.append(HUB)

        # Create edges between all nodes in truck_location_list
        # Space-time complexity is O(N^2)
        for items in self.truck_location_list:
            for items2 in self.truck_location_list:

                if items.name != items2.name:
                    weight = current_distance(items.location_id, items2.location_id)
                    edge = Edge(items, items2, weight)


                    items.adjacenciesList.append(edge)
                    # remove duplicate edges
                    items.adjacenciesList = list(set(items.adjacenciesList))

    # self.truck_location_list = list(set(self.truck_location_list))

    def print_edges(self):
        # Space-time complexity is O(N^2)
        for locations in self.truck_location_list:

            print ('\n\n\n')
            print(locations.name, ' has edges ')
            print ('\n\n')

            for edges in locations.adjacenciesList:
                print(edges.startVertex.name, edges.targetVertex.name, edges.weight)

    # OPTIMIZE TRUCK LOCATION LIST
    # This is the main algorithm of the program.
    # Space-time complexity is O(N^2)
    def optimize_truck_location_list(self):

        current_edge = ''
        distance_list = []
        # current_time = self.time
        # final_trip_time = self.time_list

        #self.truck_location_list = list(set(self.truck_location_list))
        # Set City University to 'HUB' as first location prior to while loop
        # Set all packages.status in truck to 'IN TRANSIT'
        # Space-time complexity is O(N^2)
        for item in self.truck_location_list:

            if 'HUB' == item.name:
                Current_Vertex = item

            #print items.name

        for packages in self.package_list:
            packages.delivery_status = 'IN TRANSIT'
            packages.time_delivered = 'IN TRANSIT'

        # starting distance is 0
        total_distance = 0

        # While there are still locations to visit...
        # Space-time complexity is O(N^2)
        while len(self.truck_location_list) > 1:

            min_edge = Current_Vertex.adjacenciesList[0]
            i = 0
            # In the AdjacenciesList of each locationNode in truck.location_list
            # find the min.weight (distance) in that list (next shortest path)
            # select the locationNode where weight = min
            while i < len(Current_Vertex.adjacenciesList):

                # For Developer use in testing Algorithm
                print(Current_Vertex.adjacenciesList[i].startVertex.name, Current_Vertex.adjacenciesList[
                    i].targetVertex.name, Current_Vertex.adjacenciesList[i].weight)
                if Current_Vertex.adjacenciesList[i].weight < min_edge.weight:
                    min_edge = Current_Vertex.adjacenciesList[i]

                i += 1
                print('min edge = ', min_edge.weight)


            # # Remove start vertex HUB once left HUB
            # for item in self.truck_location_list:
            #
            #     if 'HUB' == item.name:
            #         self.truck_location_list.remove(item)

            # for each location visited, add edge weight to
            # total distance travelled
            print('total distance = ', total_distance, ' + ', min_edge.weight)
            total_distance = total_distance + min_edge.weight

            distance_list.append(min_edge.weight)
            # time travelled equals distance (edge.weight) divided by speed (18 mph)
            new_time = min_edge.weight / 18
            distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
            next_time = distance_in_minutes + ':00'
            # travel time 'next_time' is added to truck.time_list at the end of each iteration
            # see line 179

            # print 'truck timelist'
            # print self.time_list

            # record the delivery time of each package when it is delivered
            current_time = datetime.timedelta()
            # Space-time complexity is O(N)
            for i in self.time_list:
                (h, m, s) = i.split(':')
                d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                #print 'd = ', d
                current_time += d
            # 'current_time' represents truck start time plus the time to travel to each node
            # through the iteration, current_time is printed at each stop
            print (self.name, current_time)

            # Once shortest path is chosen, deliver package to that location
            # Space-time complexity is O(N^2)
            for edge in Current_Vertex.adjacenciesList:

                if edge == min_edge:
                    current_edge = min_edge

                    for packages in self.package_list:

                        # if packages.address_value == Current_Vertex.address_value:
                        if packages.address_value == current_edge.startVertex.address_value:
                            packages.delivery_status = 'DELIVERED'
                            packages.time_delivered = str(current_time)
                            print('min_edge = ', min_edge.startVertex.name, min_edge.targetVertex.name, min_edge.weight)
                            print('but I delivered to current edge', current_edge.startVertex.name)
                            # self.time = str(current_time)
                        # else:
                            # print('no packages delivered here')

                        # For Developer use
                        print (packages.packageID_value, packages.address_value, packages.delivery_status,
                               packages.time_delivered)
            # remove edge paths to Current_Vertex from all other locations' adjacencyLists
            # each location is visited only once per truck route
            # Space-time complexity is O(N^2)
            for location in self.truck_location_list:

                for edge3 in location.adjacenciesList:

                    if edge3.targetVertex == Current_Vertex:
                        location.adjacenciesList.remove(edge3)

            # For Developer use
            print('startVertex to be removed is ', current_edge.startVertex.name)
            print('next stop is ', current_edge.targetVertex.name)
            # Once current location has been visited, remove location from available locations to visit
            self.truck_location_list.remove(current_edge.startVertex)

            ### For Developer use checking Algorithm ###
            print('\n locations remaining \n')

            for locations in self.truck_location_list:

                print(locations.name)
            print ('\n')
            # Once package has been delivered to current location, set min.edge (shortest path)'s
            # next location to be current location for next iteration (delivery) loop
            # Space-time complexity is O(1)
            Current_Vertex = current_edge.targetVertex
            print('next stop is ', current_edge.targetVertex.name)
            self.time_list.append(next_time)

            # Unless there remains a path to a location that matches a package with a delivery time deadline


            # deliver to 10:30 and earlier deadlines first
            # by assigning Current_Vertex to locations that match packages with delivery time deadlines.
            # As those locations are visited, they are removed from truck_location_list, until none remain
            # And this code block then becomes void, leaving Current_Vertex as the targetVertex of last edge
            # path travelled
            #
            # This code block does not affect the current time, because the algo
            # delivers all the time deadline packages before their deadline
            # but you can see difference in running this code
            # that they are delivered first before any EOD deliveries
            #
            # Space-time complexity is O(N^2)
            for locations in self.truck_location_list:
                for packages in self.package_list:

                    if locations.address_value == packages.address_value and packages.delivery_time_value != 'EOD':

                            Current_Vertex = locations

                    else:
                        pass

            # this code portion was not necessary, but could be used in future
            # to meet other time constraints
            #
            # # deliver to Public Works due by 9:00 first
            # for locations in self.truck_location_list:
            #     for packages in self.package_list:
            #
            #         if locations.address_value == packages.address_value:
            #
            #             if packages.delivery_time_value == '09:00:00':
            #                 Current_Vertex = locations
            #                 break
            # For Developer use
            print('next shortest location is', Current_Vertex.name)

        # This code not reached until truck is at the last locationNode in its location list
        # # sets the last package delivered status to 'DELIVERED'
        # Space-time complexity is O(N^2)
        for packages in self.package_list:

            if packages.address_value == Current_Vertex.address_value:
                # print 'Current Vertex is '
                # print packages.packageID_value, packages.address_value
                packages.delivery_status = 'DELIVERED'

                green_time = datetime.timedelta()
                for i in self.time_list:
                    (h, m, s) = i.split(':')
                    d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    # print 'd = ', d
                    green_time += d
                # print 'second to last trip time = ', green_time

                packages.time_delivered = str(green_time)

            print (packages.packageID_value, packages.address_value, packages.delivery_status, packages.time_delivered)

        # add distance from last delivery node back to HUB to total_distance
        # Space-time complexity is O(1)
        back_to_HUB = current_distance(0, int(self.truck_location_list.pop().location_id))
        total_distance = total_distance + back_to_HUB
        distance_list.append(back_to_HUB)

        print('total distance =', total_distance)

        # add time from last delivery node back to HUB to truck(self).time_list
        new_time = back_to_HUB / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        self.time_list.append(final_time)
        #final_trip_time includes all time from time left HUB @ truck.start_time to time back at HUB
        final_trip_time = datetime.timedelta()
        # Space-time complexity is O(N)
        for i in self.time_list:
            (h, m, s) = i.split(':')
            d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            # print 'd = ', d
            final_trip_time += d
        print ('final trip time = ', final_trip_time)

        # print self.time_list
        # print distance_list

        print ('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        print ('Final Time = ', final_trip_time)
        # This total_distance per trip is added to 'global_distance' after each trip
        # in the CSVPackages.py file, global_distance is sum of all miles travelled
        return total_distance

    # this method uses location_id's as row and column values
    # in a list matrix of a distance table
    # if you know two locations location_id's, this method
    # returns the distance between them
    # Space-time complexity is O(N)
    def current_distance(row_value, column_value):
        distance = distanceCSV[row_value][column_value]
        if distance is '':
            distance = distanceCSV[column_value][row_value]
        # print(float(distance))
        return float(distance)

    # this method not used, saved for reference
    #
    # gives total distance travelled for truck route
    # by summing the distance between each node into 'total_distance1'
    # def total_distance(self):
    #     i = 0
    #     total_distance1 = 0
    #
    #
    #     while i < len(self.truck_location_list) - 1:
    #         distance = current_distance(self.truck_location_list[i][0], self.truck_location_list[i + 1][0])
    #         i = i + 1
    #         total_distance1 += float(distance)
    #
    #     print('total distance was ', total_distance1)
    #     return total_distance1
    #
    #
    #
    # this method not used, saved for reference
    #
    # # Set LocationNodes List for the truck's route
    # # Space-time complexity is O(1)
    # def set_truck_locationNodes_list(self):
    #
    #     # Add HUB location to truck location list for starting position
    #     HUB = LocationNode(int(0), 'City University', '4001 South 700 East')
    #     self.truck_location_list.append(HUB)
    #     remove duplicate locations from packages with same location
    #     self.truck_location_list = list(set(self.truck_location_list))
    #
    #     print locations in truck to confirm route and no duplicates
    #     for items in self.truck_location_list:
    #         print items.name
    #     print '\n\n'
    #     print('total locations in truck location list = ', len(self.truck_location_list))
    #     print '\n\n\n'
