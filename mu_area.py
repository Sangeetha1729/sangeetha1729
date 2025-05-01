import numpy as np

def mu_area(X):
    # Takes three nodes of a triangle, listed as the rows
    # of a matrix X and finds the area of this triangle
    a = np.abs(np.linalg.det(np.column_stack((np.ones(3), X))) / 2)
    return a
