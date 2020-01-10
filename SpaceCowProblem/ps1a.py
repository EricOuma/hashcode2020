###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import copy, time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cowList = []
    with open(filename) as f:
        for line in f:
            # remove \n at the end and form a tuple 
            lineCopy = tuple(line.strip().split(','))
            # print(lineCopy)
            cowList.append(lineCopy)
        f.close()
    data = dict(cowList)
    # conerting the weight value to integers
    for key, value in data.items():
        data[key] = int(value)
    # print(data)
    return data

# load_cows('ps1_cow_data.txt')

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    mutable_cows = sorted(cows.items(), key=lambda v: v[1], reverse=True)
    taken_cows = []
    while len(mutable_cows)>0:
        current_weight = 0
        trip = []
        for k, v in mutable_cows[:]:
            # slicing so as to make copy of original list so as to modify it while iterating
            # https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating
            if (current_weight+v) <= limit:
                trip.append(k)
                # print('Trip:',trip)
                current_weight += v
                # print('Current Weight',current_weight)
                mutable_cows.remove((k,v))
                # print('Remaining cows',mutable_cows)
        taken_cows.append(trip)
    print('Taken Cows:',taken_cows)
    return taken_cows

# greedy_cow_transport(load_cows('ps1_cow_data.txt'), limit=10)

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    partitions_list = sorted(get_partitions(cows), key=len)
    
    taken_cows = []

    for item in partitions_list:
        if sum
        

brute_force_cow_transport(load_cows('ps1_cow_data.txt'), limit=10)

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass
