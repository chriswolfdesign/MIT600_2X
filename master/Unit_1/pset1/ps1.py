###########################
# 6.00.2x Problem Set 1: Space Cows

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

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

    cow_dict = dict()

    f = open(filename, 'r')

    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
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

    # Clone the original cows list
    temp = {}
    for item in cows:
        temp[item] = cows[item]

    all_trips = []

    # While there are still cows left to transport
    while temp:
        current_trip = []
        weight_left = limit

        while True:
            biggest_cow_name = ""
            biggest_cow_weight = 0

            # Find the largest cow
            for cow in temp:
                if temp[cow] > biggest_cow_weight and temp[cow] <= weight_left:
                    biggest_cow_name = cow
                    biggest_cow_weight = temp[cow]

            if biggest_cow_name == "":
                break
            else:
                current_trip.append(biggest_cow_name)
                weight_left -= temp[biggest_cow_name]
                del temp[biggest_cow_name]

        all_trips.append(current_trip)


    return all_trips




# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
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
    all_possibilities = get_partitions(cows)

    best_trip = []
    least_trips = len(cows) + 1

    for possibility in all_possibilities:

        for item in possibility:
            trip_weight = 0
            for cow in item:
                trip_weight += cows[cow]
            if trip_weight > limit:
                break

        if trip_weight <= limit and len(possibility) < least_trips:
            best_trip = possibility
            least_trips = len(possibility)

    return best_trip


# Problem 3
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
    start = time.time()
    greedy_cow_transport(cows, 10)
    end = time.time()

    print("Greedy transport: ", end - start)

    start = time.time()
    brute_force_cow_transport(cows, 10)
    end = time.time()

    print("Brute force transport: ", end - start)


"""
Here is some test data for you to see the results of your algorithms with.
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

if __name__ == "__main__":
    cows = load_cows("/Users/chriswolf/Documents/My_Code/Coursework/MIT600_2X/master/Unit_1/pset1/ps1_cow_data.txt")
    limit = 10
    compare_cow_transport_algorithms()
