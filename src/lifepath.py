from dices import *
from attribs import *
from factions import *
from random import choice

# This is a stub to test the procedure
def lifepath():
    print("Mutant Chronicles character creator")

    #Decision 1 - Select starting attributes
    # print("Please, select your starting attributes.")
    # attribs = load_attribs('./tables/attributes.json')
    # target = 0
    # for a in attribs:
    #     print(f'Current {a.name}: {a.value}')
    #     target += a.value

    # for a in attribs:
    #     val = int(input(f'New {a.name}: '))
    #     a.value = val

    # if not validate_attribs(attribs,target):
    #     print(f"Invalid attribs")
    #     exit()
    # else:
    #     print(attribs)

    #Decision 2 - Birth Faction
    #Step 1
    fac_herit = load_factions('./tables/factions_heritage.json')
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

    print(faction, heritage)
    #Step 2
    talent = None
    languages = None
    for f in fac_herit:
        if f['name'] == faction:
            talent = f['talent']
            languages = f['languages']
            if 'Heritage' in languages:
                languages.remove('Heritage')
                languages.append(heritage)
    

            
        


        
lifepath()