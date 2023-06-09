from dataclasses import dataclass
from typing import Any

@dataclass
class Skill:
    name: str
    expertise:int = 0
    focus:int = 0
    signature: bool = False
    
    def __hash__(self) -> int:
        return hash(self.name)
    
@dataclass
class Attribute:
    name: str
    value: int
    skills: list[Skill]

    def validate(self, min_attrib:int, max_attrib:int)->bool:
        return self.value<=max_attrib and self.value >=min_attrib
    
@dataclass
class Faction:
    id:int
    name:str
    languages:list[str]
    skills:list[Skill]
    talent:str

@dataclass
class Talent:
    skill: str
    prerequisites: list[Any]
    description: str

@dataclass
class Career:
    attrib_improvements: dict[str,int]
    mandatory_skills: list[Skill]
    elective_skills:list[Skill]
    signature_skill:str
    talents: list[Talent]
    earnings: int
    equipment:list[str]

@dataclass
class IconicCareer(Career):
    prerequisites: list[str]
    difficulty: int
    special: str
    # "era" should actually be an enum...
    era:str

@dataclass
class Character:
    attirbutes: list[Attribute]
    skills: list[Skill]
    current_faction: Faction
    background: list[Any]
    languages: list[str]
    chronicle_points: int
    traits:list[str]
    mental_wounds:int
    wounds:dict[str,int]
    soak: dict[str,int]
    melee_bonus: int
    talents:list[Talent]
    equipment: list[str]
    attacks: list[Any]
    earnings: int
    assets: int
    social_status: int
    spells:list[Any]