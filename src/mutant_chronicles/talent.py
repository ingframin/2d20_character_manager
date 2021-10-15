from dataclasses import dataclass

@dataclass
class Talent:
    name: str
    skill: str #name of the parent skill
    effect: str