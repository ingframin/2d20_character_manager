from data_model import *
from attribs import *
from abc import ABC, abstractmethod
from typing import Any

class Decision(ABC):
    
    @abstractmethod
    def setup(self,*args,**kwargs):
        pass

    @abstractmethod
    def run(self,lifepoints:int):
        pass
    
    @abstractmethod
    def next(self):
        pass

class DecOneAttribs(Decision):
    def __init__(self, filename:str) -> None:
        self.starting_attribs = load_attribs(filename)

    def setup(self,*args,**kwargs):
        pass
    
    def run(self):
        pass

    def next(self):
        pass



class CharacterBuilder:
    def __init__(self, lifepoints = 5) -> None:
        self.lifepoints = lifepoints
        self.current = 0
        self.decisions:list[Decision] = []

    def run(self):
        for d in self.decisions:
            d.setup()
            d.run()
            d.next()

