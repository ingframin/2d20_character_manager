import json
from random import choice
from dice import d6
from data_model import *
from dataclasses import dataclass

# Too much mix of load from files and random choices, it is difficult to add the custom tweaks which can be bought with life points.
# This is valid for all the files 


def load_factions(filename:str)->list[Faction]:
    with open(filename) as fp:
        data = json.load(fp)
    
    factions = []
    for d in data:
        skl = [Skill(sn) for sn in d['skills']]
        f = Faction(
            id = d['id'],
            name = d['name'],
            languages = d['languages'],
            skills=skl,
            talent=d['talent']
        )
        factions.append(f)
        
    return factions

def faction_heritage(fac_herit:list[Faction])->tuple[Faction,Faction]:
    
    faction:Faction 
    heritage:Faction 

    rnd6 = d6()
    
    if rnd6 < 4:
        #Criminal, Freelance or Microcorp
        faction = fac_herit[rnd6-1]
        heritage = choice([f for f in fac_herit if f.id>3])
    
    else:
        #Megacorp or Whitestar
        faction = choice([f for f in fac_herit if f.id>3])
        heritage = faction
    
    return (faction,heritage)

def fac_talents_lang_skills(faction:Faction, heritage:Faction)->tuple[str,set[str],set[Skill]]:
    #Step 2
    talent = faction.talent
    languages = set()
    skills = set()

    for l in faction.languages:
        if l == 'Heritage':
            for lh in heritage.languages:
                languages.add(lh)
        languages.add(l)
    
    for skill in faction.skills:
        if skill.name == 'Heritage':
            for s in heritage.skills:
                skills.add(s)
        else:
            skills.add(skill)
    
    return talent,languages,skills

def load_fact_event(filename:str, heritage_name:str)->str:
    with open(filename) as fp:
        events_table = json.load(fp)
    
    rnd6 = d6()
    
    ev:dict[str,str]
    
    for e in events_table:
        if e['roll'] == rnd6:
            ev = e
            break

    return ev[heritage_name]
    
    
    
