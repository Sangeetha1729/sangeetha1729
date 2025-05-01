import numpy as np
from scipy import sparse
from scipy.sparse import csr_matrix

def global_stiffness(elt_matrices, elements, nodes):
    nelts, m = elements.shape
    nnodes, m = nodes.shape

    # Create an empty sparse matrix with nnodes columns and rows
    Ahat = csr_matrix((nnodes, nnodes), dtype=float) 

    # Assemble the global stiffness matrix from the element matrices
    # including all the boundary nodes
    for ie in range(nelts):
        iglob = elements[ie, :]
        indeces = np.meshgrid(elements[ie, :].astype(int)-1,elements[ie, :].astype(int)-1)
        tempel = sparse.csr_matrix(elt_matrices[ie])
        Ahat[tuple(indeces)] += tempel 

    return Ahat 
