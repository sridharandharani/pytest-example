import area

import pytest

@pytest.mark.area
def test_areaofsquare():
    x = 6
    result = area.areaofsquare(x)
    assert result == x*x

@pytest.mark.peri
def test_perimeterofrectangle():
    x = 6
    y = 2
    result = area.perimeterofrectangle(x,y)
    assert result == 2*(x+y)

@pytest.mark.area
def test_areaofrectangle():
    x = 6
    y = 2
    result = area.areaofrectangle(x,y)
    assert result == x*y