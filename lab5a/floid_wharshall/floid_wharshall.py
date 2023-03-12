class FloydWarshall():

    def __init__(self, adj_matrix=[]):
        if not adj_matrix:
            raise Exception('Не предоставлена матрица смежности')
        self.adj_matrix = adj_matrix
        self.n = 0
        self.path = []

    def calculate(self):

        self.n = len(self.adj_matrix)

        cost = self.adj_matrix.copy()
        self.path = [[None for x in range(self.n)] for y in range(self.n)]

        for v in range(self.n):
            for u in range(self.n):
                if v == u:
                    self.path[v][u] = 0
                elif cost[v][u] != float('inf'):
                    self.path[v][u] = v
                else:
                    self.path[v][u] = -1

        for k in range(self.n):
            for v in range(self.n):
                for u in range(self.n):
                    if cost[v][k] != float('inf') and cost[k][u] != float('inf') \
                            and (cost[v][k] + cost[k][u] < cost[v][u]):
                        cost[v][u] = cost[v][k] + cost[k][u]
                        self.path[v][u] = self.path[k][u]

                if cost[v][v] < 0:
                    print('Обнаружен цикл')
                    return

    def print(self):

        def printPath(path, v, u, route):
            if path[v][u] == v:
                return
            printPath(path, v, path[v][u], route)
            route.append(path[v][u])

        for v in range(self.n):
            for u in range(self.n):
                if u != v and self.path[v][u] != -1:
                    route = [v]
                    printPath(self.path, v, u, route)
                    route.append(u)
                    print(
                        f'Кратчайший путь из вершины {v} в вершину {u} :', route)
