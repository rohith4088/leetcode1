from __future__ import annotations
from typing import Generic
from typing import Protocol
from typing import TypeVar

class Multiple(Protocol):
    def __mul__(self:T , x:int) -> T: ...


T = TypeVar('T')
def double(x : T) -> T:
    return x * 2
reveal_type(double([1])) 