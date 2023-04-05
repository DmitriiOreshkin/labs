from collections import defaultdict
 
class Graph:
 
    def __init__(self, vertices):
        self.V = vertices  
        self.graph = defaultdict(list)  
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
 
    def DFSUtil(self, v, visited):

        visited[v] = True
 
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

 
    def isConnected(self):
 
        visited = [False]*(self.V)
 
        for i in range(self.V):
            if len(self.graph[i]) != 0:
                break
 
        if i == self.V-1:
            return True
 
        self.DFSUtil(i, visited)
 
        for i in range(self.V):
            if visited[i] == False and len(self.graph[i]) > 0:
                return False
 
        return True

 
    def isEulerian(self):
        if self.isConnected() == False:
            return 0
        else:
            odd = 0
            for i in range(self.V):
                if len(self.graph[i]) % 2 != 0:
                    odd += 1
 
            if odd == 0:
                return 2
            elif odd == 2:
                return 1
            elif odd > 2:
                return 0
  
    def test(self):
        res = self.isEulerian()
        if res == 0:
            print("граф не является Эйлеровским")
        elif res == 1:
            print("граф имеет Эйлеров путь")
        else:
            print("граф имеет Эйлеров цикл")
 
