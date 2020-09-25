import pytest

@pytest.mark.usefixtures('setup')
class TestFixture:

    def test_fixture(self):
        print('secondly this line will execute the tests after fixture method')