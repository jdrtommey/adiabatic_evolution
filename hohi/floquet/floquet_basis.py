"""
Simply function to determine the index of a state which has been floqueed. Basis expands from
|x> to |x,q> where q is the sideband order
"""
def floquet_basis(index,q,space_length,q_bands):
    """
    finds the index of a |state,q> in the expanded floquet basis.
    finds the first index in a subblock then adds the index of the 
    state in the non-expanded basis.
    
    Parameters
    ----------
    index: int
        the index in the matrix before expanding to floquet basis
    q: int
        the sideband order
    space_length: int
        the dimension of the state-space before expansion.
    q_bands:
        the total number of q bands in space
    """
    
    if index > space_length:
        raise IndexError("index larger than dimension of space. index: " + str(index) + "space length:" + str(space_length))
        
    if abs(q) > abs(q_bands):
        raise IndexError("sideband q larger than dimension of space. index: " + str(q) + "space length:" + str(q_bands))
    
    
    return (q+q_bands)*space_length + index