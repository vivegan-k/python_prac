import pytest

@pytest.mark.one
def test_mark():
    assert '1' == str(1) # This test can be executed as "pytest pytest_prac.py -m one"

class TestClass:
    def setup_class(self):
        print('Executed setup class')

    def teardown_class(self):
        print('Executed teardown class')

    def setup_method(self):
        print('Executed setup method')

    def teardown_method(self):
        print('Executed teardown method')

    def add(self, a,b):
        return a + b

    def test_add(self):
        assert 3 + 5 == 8

    @pytest.mark.skip
    def test_add1(self):
        assert 4 + 6 == 10


    @pytest.mark.xfail
    def test_add_neg(self):
        assert 3 + 5 == 7

    @pytest.fixture
    def numbers(self):
        return range(3)
    
    def test_fixture(self, numbers):
        assert sum(numbers) == 3

    @pytest.mark.parametrize("a,b",[(2,4),(3,9)])
    def test_parameterize(self,a,b):
        assert a ** 2 == b

    