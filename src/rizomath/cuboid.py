from .interval import Interval, str_to_iv
from dataclasses import dataclass
from math import prod

@dataclass(frozen=True)
class Cuboid:
    points: list[Interval]
    value: any = None

    def volume(self) -> int:
        return prod((x.get_length() for x in self.points))
    
    def dims(self) -> int:
        return len(self.points)

    def __and__(self,other:"Cuboid") -> "Cuboid":
        """Return intersection of two cuboids of the same dimensionality"""
        if not isinstance(other,Cuboid): return None
        if other.dims() != self.dims(): return None
        #TODO - Create a __and__ overload for Interval
        intersection = [a&b for (a,b) in zip(self.points,other.points)]
        if None in intersection: return None
        return Cuboid(intersection)

def str_to_cb(s:str, val:any=None) -> Cuboid:
    """Converts a string of the type a..b c..e [...] into a Cuboid"""
    _s = s.strip()
    l = [str_to_iv(x) for x in _s.split()]
    return Cuboid(l,val)
