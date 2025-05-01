import numpy as np
from mu_area import mu_area

def elt_stiffness(elements, nodes):
    nelts, m = elements.shape  # Finds how many elements there are

    elt_matrices = [None] * nelts

    for ie in range(nelts):
        elt_matrices[ie] = np.zeros((3, 3))

        X = nodes[elements[ie].astype(int) - 1, :2]  # Coordinates of 3 nodes of element ie

        area = mu_area(X)  # Area of element ie using the determinant formula from lectures

        E = np.array([X[1, :] - X[2, :], X[2, :] - X[0, :], X[0, :] - X[1, :]])

        # Now we implement the formula given in lectures for the
        # element stiffness matrices corresponding to the Laplacian.

        Atau = np.array([[np.dot(E[0, :], E[0, :]), np.dot(E[0, :], E[1, :]), np.dot(E[0, :], E[2, :])],
                         [np.dot(E[1, :], E[0, :]), np.dot(E[1, :], E[1, :]), np.dot(E[1, :], E[2, :])],
                         [np.dot(E[2, :], E[0, :]), np.dot(E[2, :], E[1, :]), np.dot(E[2, :], E[2, :])]])

        elt_matrices[ie] = Atau / (4 * area)

    return elt_matrices
