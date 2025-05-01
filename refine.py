import numpy as np
from visited import visited

def refine(nodes, elements):

    nnodes, m = nodes.shape
    nelts, m = elements.shape

    newnodes = nodes.copy()
    newelements = np.zeros((4*nelts,3))
    inode = 1
    edgetable = np.zeros((0, 2), dtype=int)

    for ie in range(1, nelts + 1):
        newloc = np.zeros(3, dtype=int)

        for edge in range(1, 4):
            n1 = edge
            n2 = (edge % 3) + 1

            newloc[edge - 1] = visited(edgetable,
                                       elements[ie - 1, n1 - 1].astype(int)-1, elements[ie - 1, n2 - 1].astype(int)-1)

            if newloc[edge - 1] == 0:
                newloc[edge - 1] = inode
                inode += 1

                edgetable = np.vstack([edgetable, [elements[ie - 1, n1 - 1].astype(int)-1, elements[ie - 1, n2 - 1].astype(int)-1]])

                temp = np.append((nodes[elements[ie - 1, n1 - 1].astype(int) - 1, :2] +nodes[elements[ie - 1, n2 - 1].astype(int) - 1, :2])/2, 1)
    
                newnodes = np.vstack([newnodes, temp])
                

            else:
                newnodes[nnodes + newloc[edge - 1] - 1, 2] = 0

        newloc += nnodes

        for tau in range(0, 3):
            newelements[4 * (ie - 1) + tau , :3] = [elements[ie - 1, tau].astype(int),
                                                        newloc[tau].astype(int), newloc[((tau+2) % 3)].astype(int)]
            

        newelements[4 * (ie - 1) - 1, :3] = newloc[:3].astype(int)
      

    return newnodes, newelements
