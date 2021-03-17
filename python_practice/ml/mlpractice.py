import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)                #print array

print(type(arr))          #check type of arr

print(arr.dtype)

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr2 = np.array([1, 2, 3, 4], ndmin=5)

print(arr2)
print('number of dimensions :', arr2.ndim)

arr3 = np.array([1, 2, 3, 4], dtype='S')
print(arr3)
print(arr3.dtype)

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,17, 18])

newarr = arr4.reshape(2, 3, 3)

print(newarr)

print(np.__version__)     #check numpy version