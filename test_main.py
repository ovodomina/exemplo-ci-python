import main

def test_add():
    assert main.add(3, 5) == 8
    assert main.add(-1, 1) == 0
    assert main.add(0, 0) == 0