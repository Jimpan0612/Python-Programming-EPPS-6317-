"""6317 Lab4 distanceCalc
Write a function called findEucliDistance that returns the Euclidean distance between any two coordinates.
The coordinates can be supplied as parameters in the form (x1, y1, x2, y2). 
For example, if your coordinates were (312088, 60271) and (312606, 59468), your function call might look like this: findDistance(312088, 60271, 312606, 59468). 


References
-----------

"""

_auther_ = "Jim <cxp220025@utdallas.edu>"

import math

def findEucliDistance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points.

    Parameters:
    x1, y1 : float
        Coordinates of the first point.
    x2, y2 : float
        Coordinates of the second point.

    Returns:
    float
        Euclidean distance between the two points.
    """
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def findGreatDistance(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points on Earth's surface
    using the Haversine formula.

    Parameters:
    lon1, lat1 : float
        Longitude and latitude of the first point (in decimal degrees).
    lon2, lat2 : float
        Longitude and latitude of the second point (in decimal degrees).

    Returns:
    float
        Great circle distance between the two points in kilometers.
    """
    # Radius of the Earth in kilometers
    radius = 6373.0
    
    # Convert degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Calculate the distance
    distance = radius * c
    return distance

# Example usage:
if __name__ == "__main__":
    euclidean_distance = findEucliDistance(312088, 60271, 312606, 59468)
    great_circle_distance = findGreatDistance(-122.4194, 37.7749, -118.2437, 34.0522)
    
    print(f"Euclidean Distance: {euclidean_distance:.2f} units")
    print(f"Great Circle Distance: {great_circle_distance:.2f} km")
