import numpy as np

X = np.array([ [6, 70, 3], [5, 50, 6], [8, 80, 2], [4, 30, 8] ])
y = np.array([40, 65, 30, 85])
#i.
print("Shape:",X.shape," Dim:", X.ndim)
print("\n")

#ii.
print(X.T)
print("\n")

#iii.
print(X.T @ X)
print("\n")

#iv.
reverse = np.linalg.inv(X.T @ X)
print(reverse)
print("\n")


#v.
B=np.linalg.inv(X.T @ X) @ X.T @ y
print(B)
print("\n")


#vi.
'''b1 = -0.159
   b2 = 0.140
   b3 = 10.06
   '''
#vii.

new_user = np.array([5, 40, 7])
predication = new_user @ B
print(predication)
print("\n")