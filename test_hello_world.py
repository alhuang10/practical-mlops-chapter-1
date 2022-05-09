import pytest
from hello_world import add

def test_hello_world():
    assert add(3,4) == 7

@pytest.mark.xfail
def test_hello_world_fail():
    assert add(1,1) == 3