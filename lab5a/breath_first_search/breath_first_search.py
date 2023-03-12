class BFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
        self.queue = []

    def calculate(self, node):
        self.visited.append(node)
        self.queue.append(node)
        while self.queue:
            s = self.queue.pop(0)
            print(s, end=" ")
            for neighbour in self.graph[s]:
                if neighbour not in self.visited:
                    self.visited.append(neighbour)
                    self.queue.append(neighbour)
