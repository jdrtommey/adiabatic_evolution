from ..floquet_basis import *
import pytest
import numpy as np


def test_first():
    """
    1 sidebands and two dimensions.
    """
    index = 0
    q=1
    space_length=2
    q_bands=1
    
    assert floquet_basis(index,q,space_length,q_bands) == 4
    
def test_first2():
    """
    1 sidebands and two dimensions.
    """
    index = 1
    q=1
    space_length=2
    q_bands=1
    
    assert floquet_basis(index,q,space_length,q_bands) == 5

def test_first3():
    """
    1 sidebands and two dimensions.
    """
    index = 0
    q=-1
    space_length=2
    q_bands=1
    
    assert floquet_basis(index,q,space_length,q_bands) == 0
    
@pytest.mark.xfail(raises=IndexError)
def test_dim_fail():
    """
    1 sidebands and two dimensions.
    """
    index = 3
    q=-1
    space_length=2
    q_bands=1
    
    floquet_basis(index,q,space_length,q_bands)

@pytest.mark.xfail(raises=IndexError)
def test_q_fail():
    """
    1 sidebands and two dimensions.
    """
    index = 3
    q=-2
    space_length=2
    q_bands=1
    
    floquet_basis(index,q,space_length,q_bands)