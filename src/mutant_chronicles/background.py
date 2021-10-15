from dataclasses import dataclass

from mutant_chronicles.faction import Faction

@dataclass
class Background:
    social_status: int
    experience: int
    earnings: int
    influence: int
    assets: list[str]
    traits: list[str] 
    events: list[str]
    relationships: list[str]
    languages: list[str] #this should actually be a list of Enum type Language
    birth_faction: Faction