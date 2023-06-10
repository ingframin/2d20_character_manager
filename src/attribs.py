import json
from data_model import *


def load_attribs(filename:str)->list[Attribute]:
    with open(filename) as fp:
        attribs = json.load(fp)
    attributes = []
    for a in attribs:
        atr = Attribute(a['name'],a['value'],[])
        for sn in a['skills']:
            atr.skills.append(Skill(sn))
        attributes.append(atr)
    return attributes

def validate_attribs(new_attribs:list[Attribute], target:int, minv:int = 4, maxv:int = 6,)->bool:
    vals = [a.value for a in new_attribs]
    return sum(vals) == target and all([a.validate(minv,maxv) for a in new_attribs])

