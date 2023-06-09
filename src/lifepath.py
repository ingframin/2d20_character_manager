from dice import *
from attribs import *
from factions import *
from random import choice

# This is a stub to test the procedure
def lifepath():
    # print("Mutant Chronicles character creator")

    # #Decision 1 - Select starting attributes
    # print("Please, select your starting attributes.")
    # attribs = load_attribs('./tables/attributes.json')
    # target = 0
    # for a in attribs:
    #     print(f'Current {a.name}: {a.value}')
    #     target += a.value

    # # for a in attribs:
    # #     val = int(input(f'New {a.name}: '))
    # #     a.value = val

    # if not validate_attribs(attribs,target):
    #     print(f"Invalid attribs")
    #     exit()
    # else:
    #     print(attribs)

    #Decision 2 - Birth Faction
    #Step 1
    fac_herit = load_factions('./tables/factions_heritage.json')
    # print(fac_herit)
    faction, heritage = faction_heritage(fac_herit)

    print(faction, heritage)
    # #Step 2
    # talent,languages,skills = fac_talents_lang_skills(fac_herit, faction, heritage)

    # print(talent, languages, skills)
    # if len(skills)>2:
    #     print("you can only keep 2 skills and select one as signature")
    
    # event=load_fact_event('./tables/faction_events.json', heritage)    
    # print(event)
            
        


        
lifepath()