x = ["a", "b", "c", "d"]
print(x[-3:])
print(x[1:])
print(x[:])
print(x[:-1])

import numpy as np
x = np.array([10, 15, 22, 13, 17, 20, 8])
x_small = x < 17
print(type(x_small))
print(x_small)
x_small = x[x<17]
print(x_small)
