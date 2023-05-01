from flask import Flask, render_template, request, redirect, url_for, jsonify
from attribs import *
import os
import json

app = Flask(__name__,template_folder='templates',static_folder='assets')
app.config["DATA_DIR"] = os.path.join(os.getcwd(), "tables")

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
        print(len(attributes))
        update_session(attributes)
        return redirect(url_for("heritage_faction"))
        
    else:         
        try:
            ercode = f"Error: {request.args['error'] }"
        except:
            ercode = ''
        # Render template with attributes and initial values
        return render_template('start_attributes.html', attributes=attributes, error=ercode)


def update_session(data):
    for d in data:
        print(f'{d.name}: {d.value}')
    
    return "done"

@app.route("/heritage_faction")
def heritage_faction():
    return "Heritage Faction"

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
