import json
from random import choice
from dice import d6
from attribs import Skill

def load_factions(filename:str):
    with open(filename) as fp:
        data = json.load(fp)
    
    return data

def faction_heritage(fac_herit):
    faction = None
    heritage = None
    rnd6 = d6()
    match rnd6:
        case 1: 
            faction = 'Freelancer'
        case 2: 
            faction = 'Criminal'
        case 3: 
            faction = 'Microcorp'
        case _: 
            faction = choice([f['name'] for f in fac_herit if f["id"]<7])
    if rnd6 < 4:
        heritage = choice([f['name'] for f in fac_herit if f["id"]<7])
    else:
        heritage = faction
    
    return (faction,heritage)

def fac_talents_lang_skills(fac_herit, faction, heritage):
    #Step 2
    talent = None
    languages = None
    skills = []

    for f in fac_herit:
        if f['name'] == faction:
            talent = f['talent']
            languages = f['languages']
            if 'Heritage' in languages:
                languages.remove('Heritage')
                languages.append(heritage)
            for sname in f['skills']:
                if sname == 'Heritage':
                    continue
                skills.append(Skill(sname,expertise=1,focus=0))

        if f['name'] == heritage:
            for sname in f['skills']:
                skills.append(Skill(sname,expertise=1,focus=0))
    
    return talent,languages,skills

def load_fact_event(filename, heritage):
    with open(filename) as fp:
        events_table = json.load(fp)
    rnd6 = d6()
    for ev in events_table:
        if ev['roll'] == rnd6:
            return ev[heritage]
    
