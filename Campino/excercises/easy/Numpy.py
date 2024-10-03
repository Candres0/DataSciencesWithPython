import numpy as np
print(np.__version__)

array = np.arange(10)
print(array)

ar = np.full((3,3), "True", dtype=str)
print(ar)

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[arr%2 == 1])

arr1 = arr[arr%2 == 1]
new = -1
arr[arr1] = new
print(arr)