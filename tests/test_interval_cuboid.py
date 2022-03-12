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
    assert x.volume() == 8
    y = cb.str_to_cb("1..3 1..3", True)
    z = cb.str_to_cb("3..4 4..6 7..11")
    assert y.volume() == 9
    assert y.value is True
    assert x & y is None
    assert x & z is None
    x2 = cb.str_to_cb("1..1 1..1 1..1")
    assert (x & x2).volume() == 1
