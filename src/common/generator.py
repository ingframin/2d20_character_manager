from dices import *
from model import *





#Again... these should be loaded from the database

factions = {
    1: "Freelancer",
    2: "Criminal",
    3: "Microcorp",
}

corporations = {
    1: "Mishima",
    2: "Capitol",
    3: "Bauhaus",
    4: "Imperial",
    5: "Cybertronic",
    6: "Whitestar"
}

def decision1_1(attributes, increase_list, reduce_list):
    # Magic numbers are bad, however, since we focus on MC3, I am living them there.
    # I'll refactor this in a more flexible manner if we need to adapt the generator to other systems.
    for at in attributes:
        if at.name in increase_list and at.value < 6:
            at.increase()
            print(at)
        elif at.name in reduce_list and at.value > 4:
            at.decrease()
    
    

def decision1_2(attributes, inc_list, life_points):
    for at in attributes:
        if at.name in inc_list and life_points > 0 and at.value < 6:
            at.increase()
            life_points -= 1

    
def decision2_1():
    d = roll(1,d6)
    if d < 4:
        return factions[d]
    
    return corporations[d6()] 



def run():
    talents = []
    life_points = 5
    #Starting attributes
    attributes = [
        Attribute("Agility", 5),
        Attribute("Awareness", 5),
        Attribute("Coordination", 5),
        Attribute("Intelligence", 5),
        Attribute("Mental", 5),
        Attribute("Personality", 5),
        Attribute("Physique", 5),
        Attribute("Strength", 5)
    ]
    attr_names = []
    for a in attributes:
        attr_names.append(a.name)

    increase_list = []
    decrease_list = []

    print("Decision 1:")
    
    while True:
        instr = input(">>")
        if instr == 'stop':
            break
        isplit = instr.split()
        if isplit[1] in attr_names:
            if isplit[0] == 'inc':
                increase_list.append(isplit[1])
            elif isplit[0] == 'dec':
                decrease_list.append(isplit[1])
            else:
                print("unknown command")
        else:
            print("unknown attribute")
    
    decision1_1(attributes, increase_list, decrease_list)
    print(attributes)

        

if __name__ == '__main__':
    run()