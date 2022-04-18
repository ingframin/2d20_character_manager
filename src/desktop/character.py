from dataclasses import dataclass
from model import *


@dataclass
class Character:
    name: str
    faction: str
    attributes: list[Attribute]
    skills: list[Skill]
    talents: list[Talent]
    story: list[Event]

    
