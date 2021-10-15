from dataclasses import dataclass
from enum import Enum, auto

##########################################
# This is specific for Mutant Chronicles #
##########################################

class SDGM(Enum):
    SPELL = auto()
    DARK_GIFT = auto()
    MUTATION = auto()

@dataclass
class Spell:
    name: str
    s_type: SDGM
    difficulty: int
    target: str #this should maybe be an enum
    duration: int
    effect: str
