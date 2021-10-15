from dataclasses import dataclass

@dataclass
class Skill:
    name: str
    value:int
    signature: bool
    
@dataclass
class Attribute:
    name: str
    value: int
    skills: list[Skill]