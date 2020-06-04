from mymodule import meaning_of_life, meaning_of_life_url
import pytest
import numpy as np



@pytest.mark.web
def test_meaning_of_life_url():
    ret = meaning_of_life_url()
    
    
    assert isinstance(ret, str)
    assert 'Monty Python' in ret
    assert 'Meaning of Life' in ret

def test_meaning_of_life():
    n = 2
    ret = meaning_of_life(n)
    assert isinstance(ret, np.ndarray)
    assert np.unique(ret) == 42