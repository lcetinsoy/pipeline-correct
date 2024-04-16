from math_lib import moyenne

def test_moyenne():

    data = [1, 2, 3]
    assert 2 == moyenne(data) 
    assert 3 == moyenne([3, 3])