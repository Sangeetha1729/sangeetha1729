import numpy as np

def initial_mesh():
    nodes = np.array([[0.0, 0.0, 1],
                      [1.0, 0.0, 1],
                      [1.0, 1.0, 1],
                      [0.0, 1.0, 1]])

    elements = np.array([[1, 2, 3],
                         [1, 3, 4]])

    return nodes, elements
