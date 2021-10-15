from dataclasses import dataclass
from enum import Enum



@dataclass
class Skill:
    name: str
    expertise: int
    signature: bool
    focus: int

@dataclass
class Attribute:
    name: str
    value: int
    skills: list[Skill]