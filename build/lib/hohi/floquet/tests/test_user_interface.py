from ..user_interface import *
import pytest
from scipy.sparse import coo_matrix
import numpy as np
def test_coo_matrix():
    """
    check that if a coo_matrix goes in a coo_matrix
    comes out
    """
    h0 = coo_matrix(np.zeros((3,3)))
    h1 = coo_matrix(np.zeros((3,3)))
    q_bands = 2
    q_val = 0.1
    h0,h1 = floquet_matrix(h0,h1,q_bands,q_val)
    assert type(h0) == csr_matrix
    
def test_csr_matrix():
    """
    check that if a coo_matrix goes in a coo_matrix
    comes out
    """
    h0 = csr_matrix(np.zeros((3,3)))
    h1 = csr_matrix(np.zeros((3,3)))
    q_bands = 2
    q_val = 0.1
    h0,h1 = floquet_matrix(h0,h1,q_bands,q_val)
    assert type(h0) == csr_matrix
    
def test_np_matrix():
    """
    check that if a np_matrix goes in a coo
    comes out
    """
    h0 = np.zeros((3,3))
    h1 = np.zeros((3,3))
    q_bands = 2
    q_val = 0.1
    h0,h1 = floquet_matrix(h0,h1,q_bands,q_val)
    assert type(h0) == csr_matrix

@pytest.mark.xfail(raises=TypeError)
def test_wrong_matrix():
    """
    check that if a string goes in an
    error is raised
    """
    h0 = None
    h1 = np.zeros((3,3))
    q_bands = 2
    q_val = 0.1
    h0,h1 = floquet_matrix(h0,h1,q_bands,q_val)
    
@pytest.mark.xfail(raises=ValueError)
def test_wrong_matrix_shape():
    """
    check that if a string goes in an
    error is raised
    """
    h0 = np.zeros((3,4))
    h1 = np.zeros((3,3))
    q_bands = 2
    q_val = 0.1
    h0,h1 = floquet_matrix(h0,h1,q_bands,q_val)
    
@pytest.mark.xfail(raises=ValueError)
def test_wrong_matrix_shape1():
    """
    check that if a string goes in an
    error is raised
    """
    h0 = np.zeros((3,3))
    h1 = np.zeros((4,3))
    q_bands = 2
    q_val = 0.1
    h0,h1 = floquet_matrix(h0,h1,q_bands,q_val)
    
@pytest.mark.xfail(raises=ValueError)
def test_matrix_different_shape():
    """
    check that if a string goes in an
    error is raised
    """
    h0 = np.zeros((4,4))
    h1 = np.zeros((3,3))
    q_bands = 2
    q_val = 0.1
    h0,h1 = floquet_matrix(h0,h1,q_bands,q_val)

@pytest.mark.xfail(raises=TypeError)
def test_q_bands_not_int():
    """
    check that if a string goes in an
    error is raised
    """
    h0 = np.zeros((3,3))
    h1 = np.zeros((3,3))
    q_bands = [2,2]
    q_val = 0.1
    h0,h1 = floquet_matrix(h0,h1,q_bands,q_val)
    
@pytest.mark.filterwarnings()
def test_q_bands_converted():
    """
    check that if a string goes in an
    error is raised
    """
    h0 = np.zeros((3,3))
    h1 = np.zeros((3,3))
    q_bands = np.array([4])
    q_val = 0.1
    h0,h1 = floquet_matrix(h0,h1,q_bands,q_val)
    
    assert type(h0) == csr_matrix
    
@pytest.mark.filterwarnings()
def test_q_val_converted():
    """
    check that if a string goes in an
    error is raised
    """
    h0 = np.zeros((3,3))
    h1 = np.zeros((3,3))
    q_bands = 2
    q_val = 1.0
    h0,h1 = floquet_matrix(h0,h1,q_bands,q_val)
    
    assert type(h0) == csr_matrix
    
@pytest.mark.filterwarnings()
def test_q_val_converted_int():
    """
    check that if a string goes in an
    error is raised
    """
    h0 = np.zeros((3,3))
    h1 = np.zeros((3,3))
    q_bands = 2
    q_val = 1
    h0,h1 = floquet_matrix(h0,h1,q_bands,q_val)
    
    assert type(h0) == csr_matrix