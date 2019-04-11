"""
Given a H0 and a HI which is a periodic time-dependant interaction, generate the h0 and hI in the new
floquet basis of the bigger state space truncated to a certain number of sidebands. works by copying up states
and gets into a form where it can be put through the adiabatic solver.

exquisly works in csr matrices
"""
from scipy.sparse import csr_matrix,identity,block_diag,bmat

def floquet(h0,h1,q_bands,freq):
    """
    Generates new matrices for h0 and h1 in an extened Floquet basis. H0 is block
    diaognal in this basis, with the actual diagonal values shifted by the q value.
    """
    q_index = gen_q_list(q_bands)

    h0_floq = get_floq_h0(h0,q_index,freq)
    h1_floq = get_floq_h1(h1,q_index)
    
    return h0_floq,h1_floq

def gen_q_list(q_bands):
    """
    convert q_bands into a list of q_indices
    """
    lis =[]
    for i in range(-q_bands,q_bands+1):
        lis.append(i)
    return lis  #the q numbers in a list ranging from [-q,,..,0,..,q]
        
def get_h0_subblock(h0,q_val,freq):
    """
    takes a coo matrix of the h0 and an identity coo matrix
    before adding the q term 
    """
    shape = h0.shape[0]
    q_matrix = identity(shape,format = 'csr') * q_val*freq
    
    return h0.copy() + q_matrix

def get_floq_h0(h0,q_index,freq):
    """
    loops through each q value, adds a value to h0 diagonal
    and appends to list which is converted into coo diagonal
    """
    diag_blocks=[]
    for q in q_index:
        diag_blocks.append(get_h0_subblock(h0,q,freq))
        
    return block_diag(diag_blocks,format='csr')
    
def h0_offset(h0,q,q_val):
    """
    apples a shift to diagonal elements of matrix
    """
    shift = q*q_val
    
    return shifted_h0


    
def get_floq_h1(h1,q_index):
    """
    converts the h1 into the off-diagonal elements of a tridiagonal matrix. first generatesd a 
    nested list of positions of HI inside a larger sparse matix then converts this 
    to a matrix with bmat.
    """
    num_blocks = len(q_index)
    matrix_list = gen_matrix_list(h1,num_blocks)
    floq_h1 = bmat(matrix_list,format='csr')
    
    return floq_h1


def gen_h1_row(A,num_blocks,block_id):
    """
    generates a list made of either A or None, 
    """
    block_list = []
    for i in range(num_blocks):
        if i == block_id - 1 and i >=0:
            block_list.append(A)
        elif i == block_id + 1 and i < num_blocks:
                block_list.append(A)
        else:
            block_list.append(None)
    return block_list

def gen_matrix_list(A,num_blocks):
    """
    sums over the rows to produce a nested list of blocks
    """
    nested_blocks = []
    for row in range(num_blocks):
        nested_blocks.append(gen_h1_row(A,num_blocks,row))
        
    return nested_blocks
            

    