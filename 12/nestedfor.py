import numpy as np

a = range(1,7)
b  = range(8,14)

arr1 = np.array(a)
arr2 = np.array(b)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])

newarr = np.dsplit(arr ,3)

print(newarr)

