class Prima:
    def __init__(self, matrix, selected):
        self.result = {}
        self.no_edge = 0
        self.matrix = matrix
        self.selected = selected
        self.inf = float('inf')
        self.v = 5
        self.selected[0] = True

    def printResult(self):
        for key in self.result:
            print(f'ребро: {key}, вес ребра: {self.result[key]}')

    def calculate(self):
        while (self.no_edge < self.v - 1):
            minimum = self.inf
            x = 0
            y = 0
            for i in range(self.v):
                if self.selected[i]:
                    for j in range(self.v):
                        if ((not self.selected[j]) and self.matrix[i][j]):
                            if minimum > self.matrix[i][j]:
                                minimum = self.matrix[i][j]
                                x = i
                                y = j
            self.result[f'{str(x)} - {str(y)}'] = self.matrix[x][y]
            self.selected[y] = True
            self.no_edge += 1
