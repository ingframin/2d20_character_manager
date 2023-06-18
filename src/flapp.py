from flask import Flask, render_template, request, redirect, url_for, jsonify
from decisions import Decision,DecisionOneAttribs,DecisionTwoFactionHeritage
import webview
from attribs import *
from data_model import *
from factions import *
import os

# There should be a global object keeping the state of the Character sheet.
# Each step/decision should be stored in a list with the possibility of rewinding
# the process.
# The "webapp" shall read and write state information from this object.
# The object shall be serializable either in JSON or in another convenient format.
# Once the process is complete, the character sheet should be rendered as a PDF 
# with the help of PyPDF2.
# Needs a rewind funciton to reset the state of each decision and restart from the beginning  



app = Flask(__name__,template_folder='templates',static_folder='assets')
app.config["DATA_DIR"] = os.path.join(os.getcwd(), "tables")

# This should become a list of decisions

decs:dict[str,Decision] = {}

@app.route("/")
def home():
   
    return render_template("home.html")



@app.route("/standard_generation", methods=['GET','POST'])
def standard_generation():
    if 'D1' not in decs:
        # Create decision 1 if it's the first pass or after a reset
        decs['D1'] = DecisionOneAttribs(life_points=5)
    
    next_ok = 'true'
    ercode = ''
    if request.method == 'GET':
        ercode = ''
        
    if request.method == 'POST':
        
        request.form.to_dict()
        new_attribs = request.form.to_dict()
        vals = [int(new_attribs[a]) for a in new_attribs]
        if sum(vals) < 40:
            ercode = 'The sum of all the attributes should be between 40 and 45!'
            next_ok = 'false'
            
        else:

            for a in new_attribs:
                try:
                    decs['D1'].adjust_attrib(a,int(new_attribs[a]))
                except ValueError as wa:
                    ercode = str(wa)
                    next_ok = 'false'
        
        
    totpts = sum([a.value for a in decs['D1'].attributes])
    if totpts not in range(40,46):
        next_ok = 'false'
    return render_template('start_attributes.html', attributes=decs['D1'].attributes, error=ercode, total_points=totpts,next_ok=next_ok,total_LP=decs['D1'].LP)

@app.route("/faction_heritage")
def faction_heritage():
    
    if 'D2' not in decs:
        # Create decision 2 if it's the first pass or after a reset
        lp = decs['D1'].LP
        decs['D2'] = DecisionTwoFactionHeritage(life_points=lp)
    
    d2 = decs['D2']
    
    return "Decision2: Faction Heritage"

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
    # webview.create_window('Hello world', app, width=1000,height=1000)
    # webview.start()
