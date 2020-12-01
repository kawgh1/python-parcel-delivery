import csv

# Space-time complexity is O(1)
with open('Data/DistanceData.csv') as csvfile:
    distanceCSV = csv.reader(csvfile, delimiter=',')
    distanceCSV = list(distanceCSV)
    # print(distanceCSV)

# Space-time complexity is O(1)
with open('Data/Locations.csv') as csvfile:
    locationsCSV = csv.reader(csvfile, delimiter=',')
    locationsCSV = list(locationsCSV)
    # print(locationsCSV)


# Space-time complexity is O(1)
def current_distance(row_value, column_value):
    distance = distanceCSV[row_value][column_value]
    if distance is '':
        distance = distanceCSV[column_value][row_value]
    # print(float(distance))
    return float(distance)


# Space-time complexity is O(1)
def total_distance(row_value, column_value, total_distance):
    distance = distanceCSV[row_value][column_value]
    if distance is '':
        distance = distanceCSV[column_value][row_value]

    total_distance += float(distance)
    return total_distance

# current_distance(24,23)
#
# Listed below is the basic structure for Dijkstra's Algorithm
# This code was used as a foundation of the package delivery algorithm
#   though heavily modified to meet problem parameters
#
#   __Listed here for future reference__
#
# import sys
# import heapq
#
# class Edge(object):
#
#     def __init__(self, weight, startVertex, targetVertex):
#
#         self.weight = weight
#         self.startVertex = startVertex
#         self.targetVertex = targetVertex
#
#
# class Node(object):
#
#     def __init__(self, name):
#
#         self.name = name
#         self.visited = False
#         self.predecessor = None
#         self.adjacenciesList = []
#         self.minDistance = sys.maxsize
#
#     def __cmp__(self, otherVertex):
#
#         return self.cmp(self.minDistance, otherVertex.minDistance)
#
#     def __lt__(self, other):
#
#         selfPriority = self.minDistance
#         otherPriority = other.minDistance
#         return selfPriority < otherPriority
#
#
# class Algorithm(object):
#
#     def calculateShortestPath(self, vertexList, startVertex):
#
#         q = []
#         startVertex.minDistance = 0
#         heapq.heappush(q, startVertex)
#
#         while len(q) > 0:
#
#             actualVertex = heapq.heappop(q)
#
#             for edge in actualVertex.adjacenciesList:
#
#                 u = edge.startVertex
#                 v = edge.targetVertex
#                 newDistance = u.minDistance + edge.weight
#
#                 if newDistance < v.minDistance:
#
#                     v.predecessor = u
#                     v.minDistance = newDistance
#                     heapq.heappush(q, v)
#
#     def getShortestPathTo(self, targetVertex):
#
#         print("Shortest path to vertex is: ", targetVertex.minDistance)
#
#         node = targetVertex
#
#         while node is not None:
#
#             print("%s " % node.name)
#             node = node.predecessor
