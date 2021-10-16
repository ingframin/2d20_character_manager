from creation import *

def test_correct(values=(('Agility',6),('Coordination',6),('Personality',4),('Strength',4))):
    attributes = {'Agility':5, 'Awareness':5,'Coordination':5,'Intelligence':5,'Mental Strength':5, 'Personality':5,'Physique':5,'Strength':5}
    decision_one(attributes, values)
    print("Test correct input: OK")

def test_error_sum_too_high(values=(('Agility',6),('Personality',5),('Strength',3))):
    try:
        attributes = {'Agility':5, 'Awareness':5,'Coordination':5,'Intelligence':5,'Mental Strength':5, 'Personality':5,'Physique':5,'Strength':5}
        decision_one(attributes, values)
        print("Test error input: Not OK")
    except SumTooHigh as e:
        print(e)
        print(attributes)
        print("Test error input: OK")

test_correct()
test_error_sum_too_high()