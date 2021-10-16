""" Character creation """
class SumTooHigh(Exception):
    pass


def decision_one(attributes,mods):
    s = sum(attributes.values())
    for m,v in mods:
        attributes[m] = v
    
    ver = sum(attributes.values())

    if ver != s:
        err = f"Sum of attributes should be {s}:\n {attributes} \n Sum: {ver}" 
        raise SumTooHigh(err)
    
    for a in attributes:
        if attributes[a] > 6:
            raise ValueError(f"{a}: {attributes[a]}->Too high")
        elif attributes[a] < 4:
            raise ValueError(f"{a}: {attributes[a]}->Too low")
            
    return attributes






