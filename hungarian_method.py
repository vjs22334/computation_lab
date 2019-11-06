import numpy as np
from munkres import Munkres

m = Munkres()

matrix = [[9, 11, 14,11,7],
          [6, 15, 13, 13, 10],
          [12, 13, 6, 8, 8],
          [11, 9, 10, 12, 9],
          [7,12,14,10,14]]
m = Munkres()
indexes = m.compute(matrix)
print("matrix:",matrix)
total = 0
for row, column in indexes:
    value = matrix[row][column]
    total += value
    print('({}, {}) -> {}'.format(row,column,value))
print("total:",total)