import pytest


@pytest.mark.usefixtures("dataLoad")
class TestFixtureData:

    def test_DataLoad(self, dataLoad):
        print(dataLoad)