import pdfplumber
import json

pdf_file = "mutant_chronicles_rulebook.pdf"

with pdfplumber.open(pdf_file) as pdf:
    tabs = pdf.pages[50].extract_table()
    tabA = []
    tabB = []
    tabC = []
    tabD = []
    for row in tabs:
        if not row[0].isnumeric():
            continue
        tabA.append({"roll":int(row[0]),"career":row[1],"attribs":{
            "Strength":0,
            "Physique":0,
            "Agility":0,
            "Awareness":0,
            "Coordination":0,
            "Intelligence":0,
            "Mental Strength":0,
            "Personality": 0
        },
        "mandatory skills":[],
        "elective skills":[],
        "talents":[],
        "equipment":[]})

        tabB.append({"roll":int(row[0]),"career":row[2],"attribs":{
            "Strength":0,
            "Physique":0,
            "Agility":0,
            "Awareness":0,
            "Coordination":0,
            "Intelligence":0,
            "Mental Strength":0,
            "Personality": 0
        },
        "mandatory skills":[],
        "elective skills":[],
        "talents":[],
        "equipment":[]})

        tabC.append({"roll":int(row[0]),"career":row[3],"attribs":{
            "Strength":0,
            "Physique":0,
            "Agility":0,
            "Awareness":0,
            "Coordination":0,
            "Intelligence":0,
            "Mental Strength":0,
            "Personality": 0
        },
        "mandatory skills":[],
        "elective skills":[],
        "talents":[],
        "equipment":[]})

        tabD.append({"roll":int(row[0]),"career":row[4],"attribs":{
            "Strength":0,
            "Physique":0,
            "Agility":0,
            "Awareness":0,
            "Coordination":0,
            "Intelligence":0,
            "Mental Strength":0,
            "Personality": 0
        },
        "mandatory skills":[],
        "elective skills":[],
        "talents":[],
        "equipment":[]})
    
    with open("./src/tables/primary_career_tableA.json", "w") as f:
        json.dump(tabA, f, indent=4)

    with open("./src/tables/primary_career_tableB.json", "w") as f:
        json.dump(tabB, f, indent=4)

    with open("./src/tables/primary_career_tableC.json", "w") as f:
        json.dump(tabC, f, indent=4)
    
    with open("./src/tables/primary_career_tableD.json", "w") as f:
        json.dump(tabD, f, indent=4)