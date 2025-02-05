"""
create dataclass `Engine`
"""
from dataclasses import dataclass


@dataclass
class Engine:
    _volume: float
    _pistons: int


