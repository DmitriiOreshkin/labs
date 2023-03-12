import sys
from priority_queue import PriorityQueue

heap = PriorityQueue()


class Edge(object):
    def __init__(self, weight, startPeak, targetPeak):
        self.weight = weight
        self.startPeak = startPeak
        self.targetPeak = targetPeak


class Node(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacencyList = []
        self.minDistance = sys.maxsize

    def __lt__(self, other):
        selfPriority = self.minDistance
        otherPriority = other.minDistance
        return selfPriority < otherPriority


class DijkstraAlgorithm(object):

    def calculateShortestPath(self, PeakList, startPeak):
        startPeak.minDistance = 0
        heap.add(startPeak)

        while heap.container:
            actualPeak = heap.pop()

            for edge in actualPeak.adjacencyList:
                u = edge.startPeak
                v = edge.targetPeak
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.predecessor = u
                    v.minDistance = newDistance
                    heap.add(v)

    def getShortestPath(self, targetPeak):
        print(f'Кратчайший путь до вершины: {targetPeak.minDistance}')
        node = targetPeak
        print('путь:')
        while node is not None:
            print('%s' % node.name)
            node = node.predecessor
