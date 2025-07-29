from my_package import add_one
def test_add_one():
    assert add_one(1) == 2

def test_add_one_wrong():
    assert add_one(1) == 1