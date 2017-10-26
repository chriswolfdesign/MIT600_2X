from success_or_fail import *
from ps1 import *

def test_greedy_cow_transport():
    """
    Tests the accuracy of our greedy transport function.
    Passing tests will be posted in blue
    Failing tests will be posted in red
    """

    print(purple("-----------------------------------------------------------"))
    print(purple("Testing: greedy_cow_transport"))
    print(purple("-----------------------------------------------------------"))

    cows = load_cows("ps1_cow_data.txt")

    """
    Test greedy_cow_transport(cows)
    """

    function_call = "greedy_cow_transport(cows)"
    expected_result = [["Betsy"], \
                       ["Henrietta"], \
                       ["Herman", "Maggie"], \
                       ["Oreo", "Moo Moo"], \
                       ["Millie", "Milkshake", "Lola"], \
                       ["Florence"]]
    received_result = greedy_cow_transport(cows)

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

    """
    Test: greedy_cow_transport(cows, 15)
    """

    function_call = "greedy_cow_transport(cows, 15)"
    expected_result = [["Betsy", "Oreo"], \
                       ["Henrietta", "Millie"], \
                       ["Herman", "Maggie", "Moo Moo", "Milkshake"], \
                       ["Lola", "Florence"]]
    received_result = greedy_cow_transport(cows, 15)

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

    """
    Test: greedy_cow_transport(cows, 20)
    """

    function_call = "greedy_cow_transport(cows, 20)"
    expected_result = [["Betsy", "Henrietta", "Milkshake"], \
                       ["Herman", "Oreo", "Millie", "Lola"], \
                       ["Maggie", "Moo Moo", "Florence"]]
    received_result = greedy_cow_transport(cows, 20)

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

def test_brute_force_cow_transport():
    """
    Tests the accuracy of the brute force algorithm.
    Passing tests will be posted in blue.
    Failing tests will be posted in red.
    WARNING: FALSE FAILS
    Due to the randomness of this equation, you must check every possible fail
    Possible causes for false fails:
        - Cows put in same trips, but put in different order
        - Other possible acceptable trips may be returned
    """

    print(purple("-----------------------------------------------------------"))
    print(purple("Testing: brute_force_cow_transport"))
    print(purple("-----------------------------------------------------------"))


    """
    Test: brute_force_cow_transport(cows, 100)
    """

    cows = {"Moo Moo" : 50,
            "Milkshake" : 40,
            "Boo" : 20,
            "Horns" : 25,
            "Miss Bella" : 25,
            "Lotus" : 40}

    function_call = "brute_force_cow_transport(cows, 100)"

    expected_result = [["Moo Moo", "Horns", "Miss Bella"],
                       ["Milkshake", "Lotus", "Boo"]]
    received_result = brute_force_cow_transport(cows, 100)

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

    """
    Test: brute_force_cow_transport(cows, 75)
    """

    cows = {"Betsy" : 65,
            "Buttercup" : 72,
            "Daisy" : 50}

    function_call = "brute_force_cow_transport(cows, 75)"

    expected_result = [["Buttercup"],
                       ["Daisy"],
                       ["Betsy"]]
    received_result = brute_force_cow_transport(cows, 75)

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

    """
    Test: brute_force_cow_transport(cows, 145)
    """

    cows = {"Starlight" : 54,
            "Betsy" : 39,
            "Buttercup" : 11,
            "Luna" : 41}

    function_call = "brute_force_cow_transport(cows, 145)"
    expected_result = [["Starlight", "Betsy", "Buttercup", "Luna"]]
    received_result = brute_force_cow_transport(cows, 145)

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

if __name__ == "__main__":
    test_greedy_cow_transport()
    test_brute_force_cow_transport()
