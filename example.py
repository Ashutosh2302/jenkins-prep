from typing import List


l = [1, 2, 3, 4, 5]

def squares(x):
    return x*x

print(list(map(squares, l)))