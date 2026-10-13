from main import division

def test_division():
    assert division(10, 2) == 5.0
    assert division(9, 3) == 3.0
    assert division(5, 2) == 2.5
    assert division(-10, 2) == -5.0
    assert division(10, -2) == -5.0