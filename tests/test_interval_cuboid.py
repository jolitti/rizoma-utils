from src.rizomath.cuboid import Cuboid
import src.rizomath.cuboid as cb
from src.rizomath.interval import Interval
import src.rizomath.interval as iv
import pytest

def test_interval_except():
    with pytest.raises(Exception) as e_info:
        err = Interval("a","b",1)

def test_interval():
    i = Interval(1,10)
    ii = Interval(10,1)
    assert i==ii
    assert str(i) == "1..10"
    assert i.get_length() == 10
    a = Interval(1,5)
    b = Interval(5,10)
    c = Interval(2,9)
    assert a & b == Interval(5,5)
    assert c < i
    assert a <= i
    assert not a < i

def test_interval_sub():
    a = Interval(1,3)
    b = Interval(2,2)
    c = Interval(1,1)
    d = Interval(5,99)

    assert a-b == [Interval(1,1),Interval(3,3)]
    assert a-c == [Interval(2,3)]
    assert a-d == [a]
    assert a-a == []
    assert b-a == []

def test_cubo():
    x = cb.str_to_cb("1..2 1..2 1..2")
    x_equiv = cb.str_to_cb("1..2 1..2 1..2", 42)
    assert x.volume() == 8
    assert x == x
    assert x == x_equiv
    y = cb.str_to_cb("1..3 1..3", True)
    z = cb.str_to_cb("3..4 4..6 7..11")
    assert y.volume() == 9
    assert y.value is True
    assert x.value is None
    assert x & y is None
    assert x & z is None
    x2 = cb.str_to_cb("1..1 1..1 1..1")
    assert (x & x2).volume() == 1

def test_sub_cubo_sections():
    """Ensure that the correct number of sub-cuboids is formed"""
    x = cb.str_to_cb("1..3 1..3 1..3")
    y = cb.str_to_cb("2..2 2..2 2..2")
    minus = x - y
    assert len(minus) == 9+9+8
    assert sum(c.volume() for c in minus) == (x.volume() - y.volume())

def test_sub_cubo_volumes():
    x = cb.str_to_cb("1..100 1..1000 1..500")
    y = cb.str_to_cb("50..200 400..10000 -900..242") 
    diff_volume = sum(c.volume() for c in y-x)
    assert diff_volume == y.volume() - (x & y).volume()
