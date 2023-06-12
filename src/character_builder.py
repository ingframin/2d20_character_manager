from data_model import *
from attribs import *
from decisions import *

class CharacterBuilder:
    def __init__(self, lifepoints = 5) -> None:
        self.lifepoints = lifepoints
        self.current = 0
        self.decisions:list[Decision] = []
        self.state:list[Any] = []


    def run(self):
        for d in self.decisions:
            d.setup(lifepoints = self.lifepoints)
            d.run()
            self.state.append(d.next())

