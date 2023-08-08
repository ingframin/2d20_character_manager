from data_model import Attribute,Faction, Skill
from attribs import load_attribs,validate_attribs
import json
from abc import ABC

class Decision(ABC):
    pass

class DecisionOneAttribs(Decision):
    def __init__(self,life_points:int=5, attrib_file:str='./tables/attributes.json') -> None:
        self.LP = life_points
        self.attributes = self.load_attribs(attrib_file)
    
    @staticmethod
    def load_attribs(filename:str)->list[Attribute]:
        with open(filename) as fp:
            attribs = json.load(fp)
        attributes = []

        for a in attribs:
            print(a)
            atr = Attribute(a['name'],a['value'],[])
            for sn in a['skills']:
                atr.skills.append(Skill(sn))
            attributes.append(atr)
        return attributes
    
    @staticmethod
    def validate_attribs(new_attribs:list[Attribute], target:int, minv:int = 4, maxv:int = 6,)->bool:
        vals = [a.value for a in new_attribs]
        return sum(vals) == target and all([a.validate(minv,maxv) for a in new_attribs])

    def adjust_attrib(self,name:str,new_value:int, max_LP:int=5, target:int=40):
        if new_value < 4 or new_value > 6:
            raise ValueError("Attribute values must be between 4 and 6")
        
        for a in self.attributes:
            if a.name == name:
                a.value = new_value
        
        total_attr = sum([a.value for a in self.attributes])
        
        self.LP = max_LP-(total_attr- target)
        
    def __repr__(self) -> str:
        lst = [f'{a.name}:{a.value}' for a in self.attributes]
        return f'LP:{self.LP}\n'+'\n'.join(lst)
                
class DecisionTwoFactionHeritage(Decision):
    def __init__(self,life_points:int=5, fact_file:str='./tables/factions_heritage.json') -> None:
        self.LP = life_points
        # This should be another function!!
        self.facts_herit = self.load_factions(fact_file)
    
    @staticmethod
    def load_factions(filename:str)->list[Faction]:
        with open(filename) as fp:
            facts_table = json.load(fp)
        facts = []
        for f in facts_table:
            facts.append(
                Faction(f['id'],f['name'],f['languages'],f['skills'],f['talent'])
            )
        
        return facts

    def select_faction(self):
        pass

    def select_heritage(self):
        pass

    def roll_event(self):
        pass

    def assign_skills(self):
        pass
    

if __name__=='__main__':
    d1 = DecisionOneAttribs()
    print(d1.attributes)
    d1.adjust_attrib('Agility',6)
    d1.adjust_attrib('Intelligence',4)
    print(d1)
