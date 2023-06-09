from flask import Flask, render_template, request, redirect, url_for, jsonify
from attribs import *
from factions import *
import os
import json

app = Flask(__name__,template_folder='templates',static_folder='assets')
app.config["DATA_DIR"] = os.path.join(os.getcwd(), "tables")

character = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/standard_generation", methods=['GET','POST'])
def standard_generation():
    attributes = load_attribs('./tables/attributes.json')
    if request.method == 'POST':
        new_attribs = request.form.to_dict()
        checksum = 0
        for a in new_attribs:
            
            if int(new_attribs[a]) < 4 or int(new_attribs[a]) > 6:
                return redirect(url_for("standard_generation",error="Attributes should be between 4 and 6"))
            for atr in attributes:
                if atr.name == a:
                    atr.value = int(new_attribs[a])
            checksum += int(new_attribs[a])
        if checksum != 40:
            
            return redirect(url_for("standard_generation",error="The sum of all attributes should be 40!"))
        
        character['attribs'] = attributes
        return redirect(url_for("heritage_faction"))
        
    else:         
        try:
            ercode = f"Error: {request.args['error'] }"
        except:
            ercode = ''
        # Render template with attributes and initial values
        return render_template('start_attributes.html', attributes=attributes, error=ercode)



@app.route("/heritage_faction",methods=['GET','POST'])
def heritage_faction():

    fac_herit = load_factions('./tables/factions_heritage.json')
    if 'faction' not in character.keys() or 'heritage' not in character.keys():
        faction, heritage = faction_heritage(fac_herit)
        character['faction'] = faction
        character['heritage'] = heritage
    else:
        faction = character['faction']
        heritage = character['heritage']
    
    talent,languages,skills = fac_talents_lang_skills(fac_herit, faction, heritage)
    character['talents'] = [talent]
    print(talent, languages, skills)
    if len(skills)>2:
        print("you can only keep 2 skills and select one as signature")
    
    event=load_fact_event('./tables/faction_events.json', heritage)    
    print(event)
    return render_template('faction_heritage.html',faction = faction, heritage = heritage, skills=skills)



@app.route("/points_system")
def points_system():
    # Add your code for the 12 points system here
    return "12 Points System"

@app.route("/free_character")
def free_character():
    # Add your code for the free character system here
    return "Free Character"

if __name__ == "__main__":
    app.run(debug=True)
