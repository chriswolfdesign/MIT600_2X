"""
Used for running.  Do not include when submitting to the grader.
"""
class Node(object):
    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes."""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + "->"\
            + self.dest.getName()
"""
End Runner Code
"""

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        return self.weight
    def __str__(self):
        return Edge.__str__(self) + " (" + str(self.weight) + ")"

"""
Used for running.  Do not include when submitting to the grader.
"""
S = Node("ABC")
SP = Node("ACB")
WE = WeightedEdge(S, SP, "10")
print(WE)
"""
End Runner Code
"""
