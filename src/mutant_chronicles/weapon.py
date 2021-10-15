from dataclasses import dataclass

@dataclass
class Weapon:
    name: str
    Range: str
    damage: tuple[int,int]
    mode: str 
    encumberance: str
    size: int
    reliability: int
    reloads: int
    qualities: list
    #Range, encumberance and mode should be enums
