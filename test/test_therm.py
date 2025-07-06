from thermo import cel_2_far
from thermo import far_2_cel

def test_celsius():
    assert cel_2_far(100) == 212.0

def test_far():
    n = far_2_cel(120)
    assert round(n,2) == 48.89