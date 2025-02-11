import pytest
from my_rest_api.devise import Devise


@pytest.fixture
def devise1():
    return Devise('EUR','Euro',1)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_devise(devise1):
	print(">>d1=",devise1)
	print(">>type(d1)=",type(devise1))
	assert devise1.code == "EUR"