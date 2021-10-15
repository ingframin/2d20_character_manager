""" Character creation """
import json
from model.attribute import *


data = json.load(open('attributes_and_skills_MC3.json'))
attributes = []

for d in data:
    for k in d:
        attributes.append(Attribute(k,0,[]))
        for at in d[k]:
            attributes[-1].skills.append(Skill(at,0,False,0))

print(attributes[-1])



