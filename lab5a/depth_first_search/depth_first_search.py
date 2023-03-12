class DFS:
    def __init__(self, graph):
        self.graph = graph

    def calculate(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start)
        for next in self.graph[start] - visited:
            self.calculate(next, visited)
        return visited
