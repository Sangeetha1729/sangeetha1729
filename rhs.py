import numpy as np
from mu_area import mu_area

def rhs(func, N0, elements, nodes):
    nelts, m = elements.shape  # Finds how many elements there are
    nnodes, m = nodes.shape     # Finds how many nodes there are

    fhat = np.zeros(nnodes)      # Initialize with a vector of zeros

    for ie in range(1, nelts + 1):
        X = nodes[elements[ie - 1].astype(int)-1, :2]  # Coordinates of 3 nodes of element ie

        area = mu_area(X)  # Area of element ie

        for p in range(1, 4):
            i = elements[ie - 1, p - 1].astype(int)
            fhat[i - 1] += func(X[p - 1, 0], X[p - 1, 1]) * area / 3

    return fhat[N0] 
