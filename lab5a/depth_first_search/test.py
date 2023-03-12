from depth_first_search import DFS

graph = {'0': set(['3', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

graph2 = {'0': set(['1', '2']),
          '1': set(['0', '2', '4']),
          '2': set(['0']),
          '3': set(['2']),
          '4': set(['2', '3'])}

graph3 = {'0': set(['4', '2']),
          '1': set(['0', '1', '2']),
          '2': set(['4']),
          '3': set(['1']),
          '4': set(['0', '3'])}

dfs = DFS(graph)
dfs2 = DFS(graph2)
dfs3 = DFS(graph3)

dfs.calculate("0")

print()

dfs2.calculate("0")

print()

dfs3.calculate("0")
