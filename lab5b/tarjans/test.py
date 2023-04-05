from tarjans import topological_sort

graph = {
    1: [2, 3],
    2: [3, 4],
    3: [4],
    4: []
}

result = topological_sort(graph)

print(result)

graph = {
    1: [2],
    2: [3],
    3: [],
    4: [5],
    5: [6],
    6: [4]
}

result = topological_sort(graph)

print(result) 

graph = {
    1: [2],
    2: [3],
    3: [1],
    4: [1]
}

result = topological_sort(graph)
print(result)

graph = {
    1: [2],
    2: [3],
    3: [4],
    4: []
}

result = topological_sort(graph)

print(result) 