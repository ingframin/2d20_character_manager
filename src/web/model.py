from dataclasses import dataclass
from enum import Enum

@dataclass
class Attribute:
    name: str
    value: int

    def increase(self):
        self.value += 1
    
    def decrease(self):
        self.value -= 1

@dataclass
class Skill:
    name: str
    signature: bool
    expertise: int
    focus: int

@dataclass
class Talent:
    name: str
    skill: str
    effect: str
    prerequisite: str
    
@dataclass
class Weapon:
    """
    This class need refactoring:
    - range, encumberance, and size should be enums
    - reliability and damage should actually be separate objects
    - ...
    """
    w_range: str #temporary: it should be an enum
    damage: tuple[int,int]
    mode: str
    encumberance: str
    size: int
    reliability: str
    reloads: int
    qualities: list

