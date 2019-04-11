import warnings
from scipy.sparse import coo_matrix,csr_matrix
import numpy as np
from .floquet import floquet

def floquet_matrix(h0,h1,q_bands,freq):
    """
    user facing function to check the inputs to the function arent gunna fuck shit up.
    
    Parameters
    ==========
    h0: matrix 
        must be square and convertable to scipy coo_matrix
    h1: matrix 
        must be square,convertable to scipy coo_matrix, and same dimensions as h0
    q_bands: int
        symmetric number of sidebands on either side.
    freq: float
        the value to substact from diagonal elements.
        
    Returns
    =======
    h0: csr_matrix
        the non floquet term
    h1: csr_matrix
        the floquet interaction term
    """
    #check h0 and h1 can be converted into coo_matrix
    
    if type(h0) != csr_matrix:
        if type(h0) == np.ndarray or type(h0) == coo_matrix:
            try:
                h0 = csr_matrix(h0)
            except:
                raise TypeError("Could not convert h0 to csr format.")
        else:
            raise TypeError("enter H0 in numpy or csr or coo format.")
            
    if type(h1) != csr_matrix:
        try:
            h1 = csr_matrix(h1)
        except:
            raise TypeError("Could not convert h0 to coo format.")
            
    #check h0 and h1 are square and of same dimensions.
            
    if h0.shape[0] != h0.shape[1]:
        raise ValueError("h0 must be square")
    if h1.shape[0] != h1.shape[1]:
        raise ValueError("h0 must be square")
        
    if h0.shape[0] != h1.shape[0]:
        raise ValueError("h0 and h1 must be same dimensions " +str(h0.shape) +" " + str(h1.shape))
        
    # check q_bands is integer
    if type(q_bands) != int:
        try:
            old_type = type(q_bands)
            q_bands = float(q_bands)
            warnings.warn("converted q_bands from " + str(old_type)+ " to integer")
            q_bands = int(q_bands)
        except:
            raise TypeError("failed to convert q_bands to integer " +str(type(q_bands)))

    # check q_val is float
    if type(freq) != float:
        try:
            old_type = type(freq)
            freq = float(freq)
            warnings.warn("converted q_val from " + str(old_type)+ "to float")
        except:
            raise TypeError("failed to convert q_val to integer " +str(type(q_bands)))
            
    h0_floq,h1_floq = floquet(h0,h1,q_bands,freq)
        
    return h0_floq,h1_floq

    