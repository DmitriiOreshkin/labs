def topological_sort(graph):
    result = []
    visited = set()
    stack = []

    def visit(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor in graph.get(node, []):
            visit(neighbor)
        stack.append(node)

    for node in graph:
        visit(node)

    while stack:
        result.append(stack.pop())

    return result
