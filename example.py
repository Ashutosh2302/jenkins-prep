from typing import List


l = [1, 2, 3, 4, 5]

def cubes(x):
    return x*x*x

print(list(map(cubes, l)))