#Fixture is used to execute pre-reqs before some test, like connections to databases, e-mail servers, etc.
#so setup and tear down the methods after execution
#yeld executes the subsequently tasks, like if it is an iterator
#confitest is a file that allows the execution of fixtures in all methods that invokes it
#also you can define fixture for classes so the fixtures will be executed in every class methods
#you also com define "scope='class'" to execute the yeld just once
#DataDriven and parametrization both can be instanciated using tuples
import pytest


@pytest.fixture(scope='class')
def setup():
    print('Firstly will be printed this line')
    yield
    print('Finally this line will finish the execution')


@pytest.fixture()
def dataLoad():
    print('Load content of fixture')
    return ['Yago', 'Gomes', 'testDataLoad.com']

@pytest.fixture(params=['Chrome', 'Firefox'])
def crossBrowser(request):
    return request.param