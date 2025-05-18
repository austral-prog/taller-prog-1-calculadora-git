import pytest
from operaciones.especiales import factorial

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    
def test_factorial_negativo():
    with pytest.raises(ValueError):
        factorial(-1)
