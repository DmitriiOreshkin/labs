from prima import Prima

matrix = [[0, 9, 75, 0, 0],
          [9, 0, 95, 19, 42],
          [75, 95, 0, 51, 66],
          [0, 19, 51, 0, 31],
          [0, 42, 66, 31, 0]]

selected = [0, 0, 0, 0, 0]

c = Prima(matrix, selected)
c.calculate()
c.printResult()
