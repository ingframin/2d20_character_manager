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

    def setup(self,*args,**kwargs):
        pass
    
    def run(self):
        pass

    def next(self):
        pass

class DecTwoBirthFaction(Decision):

    def setup(self,*args,**kwargs):
        pass
    
    def run(self):
        pass

    def next(self):
        pass

class DecThreeStatus(Decision):

    def setup(self,*args,**kwargs):
        pass
    
    def run(self):
        pass

    def next(self):
        pass

class DecFourEnvironment(Decision):

    def setup(self,*args,**kwargs):
        pass
    
    def run(self):
        pass

    def next(self):
        pass

class DecFiveEducation(Decision):

    def setup(self,*args,**kwargs):
        pass
    
    def run(self):
        pass

    def next(self):
        pass

class DecSixPrimaryCareer(Decision):

    def setup(self,*args,**kwargs):
        pass
    
    def run(self):
        pass

    def next(self):
        pass

class DecSevenIconicCareer(Decision):

    def setup(self,*args,**kwargs):
        pass
    
    def run(self):
        pass

    def next(self):
        pass

class DecEightFinalCustomization(Decision):

    def setup(self,*args,**kwargs):
        pass
    
    def run(self):
        pass

    def next(self):
        pass