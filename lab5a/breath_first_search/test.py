from breath_first_search import BFS

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


bfs = BFS(graph)
bfs.calculate('A')
