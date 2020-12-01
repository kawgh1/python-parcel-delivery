### Core Algorithm Overview
#### Stated Problem:

The purpose of this project is to create an algorithm that successfully determines the optimal or near-optimal route 
for package delivery by the [removed] Parcel Service in [removed], using a common
 programming language; Python 3.7 in this case. The algorithm and code should be designed in a way so as to be scalable 
 and replicable for use by [removed] in other cities, with minimal rework or modification. In this scenario there are 40 
 packages, many with special condition parameters, to be delivered to 26 different locations as quickly as possible 
 while meeting the package parameters, such as delivery time deadlines, delays or groups of packages, etc. [removed] has 
 two drivers and three trucks with which to deliver all the packages.
 
 
The proposed solution to this problem will first sort and separate the packages by their requirements and load them 
on to the trucks as truck space is available. Once loaded, a greedy algorithm (based on Dijkstra’s Shortest Path 
algorithm) will determine which packages need to be delivered first (time deadlines) and then determine which 
location has the next shortest path from the last delivery location in a loop-like fashion until no packages remain. 
Once a truck is empty it will return to the ‘HUB’ to either pick up more packages if needed or simply wait for the 
other truck to return.

This program was written in Python 3.7 on a Windows 8 OS using PyCharm IDE. That is the ideal setup for this program to
work correctly. To run, in the terminal enter "python main.py".