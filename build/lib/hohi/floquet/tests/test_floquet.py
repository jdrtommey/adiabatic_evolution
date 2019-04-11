from ..floquet import *
import pytest
import scipy.sparse as sparse

def test__get_q_list():
    q_bands = 1
    q_index = gen_q_list(q_bands)
    assert q_index[0] == -1 and q_index[2] == 1 and len(q_index) == 3
    
def test__get_q_list1():
    q_bands = 10
    q_index = gen_q_list(q_bands)
    assert q_index[0] == -10 and q_index[20] == 10 and len(q_index) == 21


def test_subblock():
    """
    given a h0 with 2 on diagonals will
    return one with 1s
    """
    h0 = sparse.diags([2.0,2.0,2.0,2.0],format='csr')
    q_val = -1
    freq = 1.0
    
    my_new = get_h0_subblock(h0,q_val,freq)
    
    assert my_new.diagonal()[0] == 1.0 
    
    
def test_subblock1():
    """
    given a h0 will return a matrix of same dimensions
    """
    h0 = sparse.diags([1.0,2.0,3.0,4.0,5.0,6.0],format='csr')
    q_val = -1
    freq = 1.0
    
    my_new = get_h0_subblock(h0,q_val,freq)
    
    assert my_new.shape[0] == h0.shape[0]
    
def test_subblock_q0():
    """
    given a h0 with 2 on diagonals will
    return one with 1s
    """
    h0 = sparse.diags([1.0,2.0,3.0,4.0,5.0,6.0],format='csr')
    q_val = 0
    freq = 1.0
    
    my_new = get_h0_subblock(h0,q_val,freq)
    
    assert my_new.diagonal()[0] == h0.diagonal()[0]


def test_correct_dimension():
    """
    if have 5 q values -2,-1,0,1,2 and a basic dimension
    of 3 should get a 5*3 = 15 sized matrix out.
    """
    q_index =[-2,-1,0,1,2]
    h0 = sparse.diags([1.0,2.0,3.0],format='csr')
    freq = 1.0
    
    new_matrix = get_floq_h0(h0,q_index,freq)
    
    assert new_matrix.shape[0] == 15 and new_matrix.shape[1]==15
    
def test_correct_edeg_vals():
    """
    if have 5 q values -2,-1,0,1,2 and a basic dimension
    of 3 should get a 5*3 = 15 sized matrix out, first element
    should be -2*1.0 + 1.0 == -1.0 and last should be +2*1.0 + 3.0 == 5.0
    """
    q_index =[-2,-1,0,1,2]
    h0 = sparse.diags([1.0,2.0,3.0],format='csr')
    freq = 1.0
    
    new_matrix = get_floq_h0(h0,q_index,freq)
    
    assert new_matrix.toarray()[0][0] == -1.0 and new_matrix.toarray()[14][14]==5
    
    
def test_gen_h1_row():
    """
    test that outcome for the first row is [None,'foo',None,None]
    """
    A = 'foo'
    num_blocks = 4
    block_id = 0
    lis = gen_h1_row(A,num_blocks,block_id)
    
    assert lis[0]==None and lis[1]=='foo' and lis[2]==None and lis[3]==None
    
def test_gen_h1_row1():
    """
    test that outcome for the first row is [None,'foo',None,None]
    """
    A = 'foo'
    num_blocks = 4
    block_id = 3
    lis = gen_h1_row(A,num_blocks,block_id)
    
    assert lis[0]==None and lis[1]==None and lis[2]=='foo' and lis[3]==None
    
def test_gen_h1_row2():
    """
    test that outcome for the third row is [None,'foo',None,'foo']
    """
    A = 'foo'
    num_blocks = 4
    block_id = 2
    lis = gen_h1_row(A,num_blocks,block_id)
    
    assert lis[0]==None and lis[1]=='foo' and lis[2]==None and lis[3]=='foo'
    
def test_gen_h1_smallest():
    """
    test that outcome for the first row is [None,'foo']
    """
    A = 'foo'
    num_blocks = 2
    block_id = 0
    lis = gen_h1_row(A,num_blocks,block_id)
    
    assert lis[0]==None and lis[1]=='foo'
    
def test_gen_h1_smallest1():
    """
    test that outcome for the second row is ['foo',None]
    """
    A = 'foo'
    num_blocks = 2
    block_id = 0
    lis = gen_h1_row(A,num_blocks,block_id)
    
    assert lis[0]==None and lis[1]=='foo'
    

def test_gen_matrix_list():
    """
    given 5 blocks and 'foo' will generate nested list of
    5 other lists 
    """
    a='foo'
    num = 5
    lists = gen_matrix_list(a,num)
    assert len(lists) ==5
    
def test_gen_matrix_list1():
    """
    given 5 blocks and 'foo' will generate nested list of
    5 other lists, in first list get [None,'foo',None,None,None]
    """
    a='foo'
    num = 5
    lists = gen_matrix_list(a,num)
    assert lists[0][0]== None and lists[0][1]=='foo'
    
def test_gen_matrix_list2():
    """
    given 5 blocks and 'foo' will generate nested list of
    5 other lists, in third list get [None,'foo',None,'foo',None]
    """
    a='foo'
    num = 5
    lists = gen_matrix_list(a,num)
    assert lists[2][0] == None and lists[2][1]=='foo'  and lists[2][2]==None
    
def test_gen_matrix_list_smallest():
    """
    given 5 blocks and 'foo' will generate nested list of
    5 other lists, in third list get [None,'foo',None,'foo',None]
    """
    a='foo'
    num = 2
    lists = gen_matrix_list(a,num)
    
    assert lists[0][1] == 'foo' and lists[0][0]==None
    
def test_gen_matrix_list_nearly():
    """
    given 5 blocks and 'foo' will generate nested list of
    5 other lists, in third list get [None,'foo',None,'foo',None]
    """
    a='foo'
    num = 3
    lists = gen_matrix_list(a,num)
    
    assert lists[2][1] == 'foo' and lists[2][2]==None
    
def test_gen_matrix_list_smallest1():
    """
    given 5 blocks and 'foo' will generate nested list of
    5 other lists, in third list get [None,'foo',None,'foo',None]
    """
    a='foo'
    num = 2
    lists = gen_matrix_list(a,num)
    
    assert lists[1][0] == 'foo' and lists[1][1]==None
    
    

def test_get_floq_h1():
    """
    expect to have a matrix of dimension (2*3) by (2*3)
    """
    h1 = sparse.diags([1.0,2.0],format='csr')
    q_index = [-1,0,1]
    
    floq_h1 = get_floq_h1(h1,q_index)
    
    assert floq_h1.shape[0] == 6 and floq_h1.shape[1] == 6
    
def test_get_floq_h11():
    """
    expect to have a matrix of dimension (2*3) by (2*3)
    want to have 8 non zero elements
    """
    h1 = sparse.diags([1.0,2.0],format='csr')
    q_index = [-1,0,1]
    
    floq_h1 = get_floq_h1(h1,q_index)
    
    assert floq_h1.nnz ==8
    
def test_get_floq_h111():
    """
    expect to have a matrix of dimension (2*3) by (2*3)
    want to have 8 non zero elements located at [2,0],[3,1],[4,2],[5,3]
    """
    h1 = sparse.diags([1.0,2.0],format='csr')
    q_index = [-1,0,1]
    
    floq_h1 = get_floq_h1(h1,q_index)
    f = floq_h1.toarray()
    assert f[2][0] == f[0][2] == f[4][2] == f[2][4] == 1.0 and\
           f[5][3] == f[3][5] == f[3][1] == f[1][3] == 2.0
    
def test_get_floq_large():
    """
    diagonal on interaction of length 10, and 11 q subspaces, 
    there expect 200 non-zero values
    """
    h1 = sparse.diags([1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0],format='csr')
    q_index = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
    
    floq_h1 = get_floq_h1(h1,q_index)
    assert floq_h1.nnz == 200
    
    
def test_floquet():
    """
    given a h0 and h1 check after being floqueted they both have the correct
    size and shape and are equal
    """
    h0 = sparse.diags([1.0,2.0,3.0],format='csr')
    h1 = sparse.diags([1.0,2.0,3.0],format='csr')
    q_bands = 2
    freq = 0.1
    
    h0_floq,h1_floq = floquet(h0,h1,q_bands,freq)
    
    assert h0_floq.shape[0]==h0_floq.shape[1]==h1_floq.shape[0]==h1_floq.shape[1]==15
    
def test_floquet_nums():
    """
    given a h0 and h1 check after being floqueted they both have the correct
    size and shape and are equal. h0 has 3*5 non-zero, h1 has 24
    """
    h0 = sparse.diags([1.0,2.0,3.0],format='csr')
    h1 = sparse.diags([1.0,2.0,3.0],format='csr')
    q_bands = 2
    freq = 0.1
    
    h0_floq,h1_floq = floquet(h0,h1,q_bands,freq)
    
    assert h0_floq.nnz == 15 and h1_floq.nnz == 24

def test_floquet_values():
    """
    given a h0 and h1 check after being floqueted they both have the correct
    size and shape and are equal
    """
    h0 = sparse.diags([1.0,2.0,3.0],format='csr')
    h1 = sparse.diags([1.0,2.0,3.0],format='csr')
    q_bands = 2
    freq = 0.1
    
    h0_floq,h1_floq = floquet(h0,h1,q_bands,freq)
    
    h = h0_floq.toarray()
    
    assert h[0][0] == 0.8 and h[1][1]==1.8 and h[2][2]==2.8 and h[12][12] == 1.2 and h[13][13]==2.2 and h[14][14]==3.2
    
def test_floquet_values1():
    """
    given a h0 and h1 check after being floqueted they both have the correct
    size and shape and are equal
    """
    h0 = sparse.diags([1.0,2.0,3.0],format='csr')
    h1 = sparse.diags([1.0,2.0,3.0],format='csr')
    q_bands = 2
    freq = 0.1
    
    h0_floq,h1_floq = floquet(h0,h1,q_bands,freq)
    
    h = h1_floq.toarray()
    
    assert h[0][3] == 1.0 and h[4][1]==2.0 and h[5][2]==3.0 