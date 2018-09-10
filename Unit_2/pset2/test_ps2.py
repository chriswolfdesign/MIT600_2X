from ps2 import *
from success_or_fail import *

def testIsPositionInRoom():

    print()
    print(purple("-----------------------------------------------------------"))
    print(purple("testIsPositionInRoom()"))
    print(purple("-----------------------------------------------------------"))

    room = RectangularRoom(4, 5)
    pos = Position(2.0, 3.0)
    function_call = "RectangularRoom(4, 5).isPositionInRoom(Position(2.0, 3.0))"
    expected_result = True
    received_result = room.isPositionInRoom(pos)

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)


    pos = Position(0.0, 0.0)
    function_call = "RectangularRoom(4, 5).isPositionInRoom(Position(0.0, 0.0))"
    expected_result = True
    received_result = room.isPositionInRoom(pos)

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

    pos = Position(-2.0, 0.0)
    function_call = "RectangularRoom(4, 5).isPositionInRoom(Position(-2.0, 0.0))"
    expected_result = False
    received_result = room.isPositionInRoom(pos)

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

    pos = Position(0.0, 12.0)
    function_call = "RectangularRoom(4, 5).isPositionInRoom(Position(0.0, 12.0))"
    expected_result = False
    received_result = room.isPositionInRoom(pos)

    if expected_result == received_result:
        success(function_call)
    else:
        fail(function_call, expected_result, received_result)

def testGetRandomPosition():
    print()
    print(purple("-----------------------------------------------------------"))
    print(purple("testGetRandomPosition()"))
    print(purple("-----------------------------------------------------------"))

    room = RectangularRoom(3, 4)

    print()
    print("Room(3, 4)")

    for i in range(15):
        print(room.getRandomPosition())

    print()
    room = RectangularRoom(5, 6)
    print("room(5, 6)")

    for i in range(15):
        print(room.getRandomPosition())

if __name__ == "__main__":
    testIsPositionInRoom()
    testGetRandomPosition()
