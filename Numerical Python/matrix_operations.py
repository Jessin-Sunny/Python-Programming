import numpy as np
from numpy.linalg import inv, det
A = np.array([(21, 36), (1, 2)])
print("A \n", A)
B = np.array([(2, 4), (10, 20)])
print("B\n",B)
print("Transpose of A\n", A.transpose())
print("Inverse of A\n", inv(A))
print("Trace of A\n", np.trace(A))
print("Determinant of A\n", det(A))
print("Matrix Multiplication A*B\n", A.dot(B))
