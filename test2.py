import numpy as np

a = np.array([[1, 2, 3], [0, 1, 2], [2, 0, 0]])
b = np.array([[1], [1], [0]])

Xt = np.linalg.solve(a, b)

print(Xt)
