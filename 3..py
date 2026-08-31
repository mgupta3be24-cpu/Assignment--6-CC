import numpy as np

#i.
original = np.array([1, 2, 3, 4, 5, 6])
#ii.
subset=original[1:4]
print(subset)
print("\n")
#iii.
subset[0] = 999
print(original)
print(subset)
print("\n")
#iv.
subset1= original[1:4].copy()

subset1[0] = 500
print(original)
print(subset1)
print("\n")
#v.
matrix = np.arange(1, 13).reshape(3, 4)
print(matrix)
print("\n")

#vi.
#a.
print(matrix[0])
#b
print(matrix[-1])
#c.
print(matrix[:, 1])
#d.
print(matrix[0:2, 1:3])
print("\n")

#vii.
flat1 = matrix.flatten()
print(flat1)

flat2 = matrix.ravel()
print(flat2)
print("\n")

#viii.
flat2[0] = 100
print(matrix)
print(flat2)
print("\n")

#ix.
flat1 = matrix.flatten()
flat1[0] = 200
print(matrix)
print(flat1)
print("\n")


#x.
print(matrix.shape)
print(matrix.ndim)
print(matrix.size)
print(matrix.dtype)