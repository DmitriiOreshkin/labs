from fleury import Graph, node_dict_to_list

nodes = {
        0: (1, 2),
        1: (0, 2, 3, 4),
        2: (0, 1, 3, 5),
        3: (1, 2, 4, 5),
        4: (1, 3, 5),
        5: (2, 3, 4)
}
nodes = node_dict_to_list(nodes)
graph = Graph(nodes)
path = graph.get_fleury_path()
print(" -> ".join(path))


nodes = {
        0: (1, 2),
        1: (0, 3),
        2: (0, 3),
        3: (1, 2)
}
nodes = node_dict_to_list(nodes)

graph = Graph(nodes)
path = graph.get_fleury_path()
print(" -> ".join(path))