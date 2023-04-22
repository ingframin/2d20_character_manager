import json

def load_factions(filename:str):
    with open(filename) as fp:
        data = json.load(fp)
    
    return data
        

    