from abc import ABC, abstractmethod
from typing import Any
from data_model import *
from attribs import *

class Decision(ABC):
    
    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def next(self):
        pass

class DecOneAttribs(Decision):

    def __init__(self,lifepoints:int,attrib_path:str)->None:
        self.LP = lifepoints
        self.attribs = load_attribs(attrib_path)
    
    def run(self):
        # 1) ask for adjustments
        new_attribs = []
        for a in self.attribs:
            print(a.name,'\t',a.value)
            newval = input("Change value? ")
            if newval.isdigit():
                nwa = Attribute(a.name,int(newval),a.skills)
                while not nwa.validate(4,6):
                    newval = input("Change value? ")
                    nwa = Attribute(a.name,int(newval),a.skills)
                new_attribs.append(nwa)
            else:
                new_attribs.append(a)
        print(new_attribs)
        # 2) spend LP for adjustments

    def next(self):
        pass

    def __repr__(self) -> str:
        return f"LP:{self.LP},\n {self.attribs}"
    
