import matplotlib.pyplot as plt
import numpy as np

def visualise(nodes, elements):
    nelts, m = elements.shape   # Finds the number of elements

    # Visualizes the mesh specified by the data in nodes and elements
    plt.figure()

    for ie in range(1, nelts + 1):
        plt.plot(nodes[elements[ie - 1, [0, 1, 0]].astype(int)-1, 0], nodes[elements[ie - 1, [0, 1, 0]].astype(int)-1, 1],
                 'k-', linewidth=2)
        plt.plot(nodes[elements[ie - 1, [1, 2, 1]].astype(int)-1, 0], nodes[elements[ie - 1, [1, 2, 1]].astype(int)-1, 1],
                 'k-', linewidth=2)
        plt.plot(nodes[elements[ie - 1, [0, 2, 0]].astype(int)-1, 0], nodes[elements[ie - 1, [0, 2, 0]].astype(int)-1, 1],
                 'k-', linewidth=2)

    # Plot the nodes on top: use a magenta dot for Dirichlet nodes
    # and a blue dot for non-Dirichlet nodes

    # Find Dirichlet nodes
    ND = np.where(nodes[:, 2] == 1)[0]
    # Plot them
    plt.plot(nodes[ND, 0], nodes[ND, 1], 'm.', markersize=10)

    # Find non-Dirichlet nodes
    N0 = np.where(nodes[:, 2] != 1)[0]
    # Plot them
    plt.plot(nodes[N0, 0], nodes[N0, 1], 'b.', markersize=10)

    plt.show()

# Example usage:
# visualise(nodes, elements)
