#Every pystest or test in pthon must start or end with "_" (underscore)
#any method must start with "test"
#Any code must be wrapped in method only
#you can run some tests on the terminal running py.test <filename>
#methods name must have sense
#-k stands for methods name execution
#-s logs in output
#-v stands for more metadata
#you can mark (tag) test @pytest.mark.smoke and run with "-m"
#you can skip tests using @pystes.mark.skip
#run your tests with "--html=<filename>" creates an reports to show in the browser

import pytest

@pytest.mark.smoke
def test_first():
    msg = 'hello'
    assert 'hello' in msg

def test_num(setup):
    a = 5
    b = 4
    assert a + b == 9, "addition doesn't match"


def test_crossBrowser(crossBrowser):
    print(crossBrowser)