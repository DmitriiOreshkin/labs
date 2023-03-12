from floid_wharshall import FloydWarshall

inf = float('inf')

matrix = [
    [0, inf, -2, inf],
    [4, 0, 3, inf],
    [inf, inf, 0, 2],
    [inf, -1, inf, 0]
]

matrix1 = [
    [1, 3, 4, -4],
    [4, 0, 3, inf],
    [inf, 0, 0, 2],
    [inf, -1, inf, 0]
]

matrix2 = [
    [5, inf, -2, 10],
    [4, inf, 3, inf],
    [3, 6, 0, 2],
    [inf, -3, inf, 0]
]

paths = FloydWarshall(matrix)
paths1 = FloydWarshall(matrix1)
paths2 = FloydWarshall(matrix2)

paths.calculate()
paths.print()

print()

paths1.calculate()
paths1.print()

print()

paths2.calculate()
paths2.print()
