from math_series import __version__
from math_series.series import sum
from math_series.series import fiboseries
from math_series.series import lucasSeries
def test_version():
    assert __version__ == '0.1.0'

def test_febonacci():
    expected = 1
    actual = fiboseries(1)
    assert actual == expected

def test_sum():
    expected=3
    actual=sum(1,0,3)
    assert actual == expected

def test_lucasSeries():
    expected=4
    actual=lucasSeries(3)
    assert actual == expected