from fuel import convert, gauge
import pytest

def test_conver():
    assert convert('1/2') == (1, 2)
    assert convert('2/3') == (2, 3)
    with pytest.raises(ValueError):
        assert convert('2/1') is ValueError
    with pytest.raises(ValueError):
        assert convert('1/-2') is ValueError
    with pytest.raises(ZeroDivisionError):
        assert convert('1/0') is ZeroDivisionError
def test_gauge():
    assert gauge(76) == '76%'
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(65) == '65%'

test_conver()
test_gauge()