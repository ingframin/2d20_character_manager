from dice import *
from factions import *
from random import choice
from data_model import Attribute, Skill
import json



def validate_attribs(attribs, target):
    vals = [a.value for a in attribs]
    return sum(vals) == target

def decision_one(attribs,lifepoints):
    new_attribs = attribs
    target = 40
    use_lp = input("Use Life Points? (y/n)")
    if use_lp == 'y':
        how_many = int(input("How many? "))
        target += how_many
        lifepoints -= how_many

    while not validate_attribs(new_attribs,target):
        for a in new_attribs:
            increase = input(f'Increase {a.name}? (y/n)')
            if increase == 'y':
                a.value += 1
        for a in new_attribs:
            decrease = input(f'Decrease {a.name}? (y/n)')
            if decrease == 'y':
                a.value -= 1
        print(sum([a.value for a in new_attribs]))
    
    return new_attribs, lifepoints

def load_factions():
    with open('./tables/factions_heritage.json') as fp:
        data = json.load(fp)
    return [Faction(f['id'],f['name'],f['languages'],f['skills'],f['talent']) for f in data]

def decision_two(attribs,lifepoints,skills):
    new_attribs = attribs
    new_skills = []
    factions = load_factions()
    faction_roll = d6()
    heritage = None
    if faction_roll in [1,2,3]:
        faction = factions[faction_roll-1]
        heritage = factions[2+d6()]
    elif faction_roll in [4,5,6]:
        faction = factions[2+d6()]
        heritage = faction
    languages = heritage.languages[0]
    for s in heritage.skills:
        new_skills.append(Skill(s))

    return new_attribs, new_skills

# This is a stub to test the procedure
def lifepath():
    
    lifepoints = 5
    attribs = [
    Attribute("Strength",5,[]),
    Attribute("Physique",5,[]),
    Attribute("Agility",5,[]),
    Attribute("Awareness",5,[]),
    Attribute("Coordination",5,[]),
    Attribute("Intelligence",5,[]),
    Attribute("Mental Strength",5,[]),
    Attribute("Personality",5,[])]

    skills = [
    Skill("Survival"),
    Skill("Acrobatics"),
    Skill("Willpower"),
    Skill("Pilot"),
    Skill("Stealth"),
    Skill("Lifestyle"),
    Skill("Thievery"),
    Skill("Ranged Rewards"),
    Skill("Heavy Rewards"),
    Skill("Gunnery"),
    Skill("Observation"),
    Skill("Insight"),
    Skill("Linguistics"),
    Skill("Science"),
    Skill("Mechanics"),
    Skill("Psychotherapy"),
    Skill("Medicine"),
    Skill("Treatment"),
    Skill("Vacuum"),
    Skill("Unarmed Combat"),
    Skill("Close Combat"),
    Skill("Command"),
    Skill("Persuade"),
    Skill("Animal Handling"),
    Skill("Education"),
    Skill("Lifestyle"),
    Skill("Persuade"),
    Skill("Command")
    ]
    talents = []
    print("Mutant Chronicles character creator")
    attribs1, lifepoints1 = decision_one(attribs,lifepoints)
    print(attribs1)
    print(lifepoints1)


        
lifepath()