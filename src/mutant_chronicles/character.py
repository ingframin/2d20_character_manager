from dataclasses import dataclass, field

from mutant_chronicles.background import Background
from .faction import Faction
from .attribute import Attribute, Skill
from .talent import Talent
from .background import Background
from .spell import Spell

@dataclass
class Character:
    name: str
    current_faction: Faction = None
    attributes: list[Attribute] = field(default_factory=list)
    skills: list[Skill] = field(default_factory=list)
    talents: list[Talent] = field(default_factory=list)

    #to be split by body part
    wounds: list = field(default_factory=list)
    soak: list = field(default_factory=list)

    belongings: list = field(default_factory=list)
    background: Background = None
    spells: list[Spell] = None