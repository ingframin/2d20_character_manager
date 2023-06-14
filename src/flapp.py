from flask import Flask, render_template, request, redirect, url_for, jsonify
import webview
from attribs import *
from data_model import *
from factions import *
import os
import json
app = Flask(__name__,template_folder='templates',static_folder='assets')
app.config["DATA_DIR"] = os.path.join(os.getcwd(), "tables")

@app.route("/")
def home():
    attribs = load_attribs('./tables/attributes.json')
    
    return render_template("home.html", attributes=attribs)


character = {}

@app.route("/standard_generation", methods=['GET','POST'])
def standard_generation():
    
    attributes = load_attribs('./tables/attributes.json')
    next_ok = 'true'
    if request.method == 'GET':
        ercode = ''
        
        
    if request.method == 'POST':
        request.form.to_dict()
        new_attribs = request.form.to_dict()
        for a in new_attribs:
            for atr in attributes:
                if atr.name == a:
                    atr.value = int(new_attribs[a])

        if validate_attribs(attributes,40):
            ercode = 'Success!'
            next_ok = 'false'
        else:
            ercode = "The sum of all attributes should be 40!"
        
    totpts = sum([a.value for a in attributes])
    return render_template('start_attributes.html', attributes=attributes, error=ercode, total_points=totpts,next_ok=next_ok)
        # checksum = 0
        # for a in new_attribs:
            
        #     if int(new_attribs[a]) < 4 or int(new_attribs[a]) > 6:
        #         return redirect(url_for("standard_generation",error="Attributes should be between 4 and 6"))
        #     for atr in attributes:
        #         if atr.name == a:
        #             atr.value = int(new_attribs[a])
        #     checksum += int(new_attribs[a])
    #     if checksum != 40:
            
    #         return redirect(url_for("standard_generation",error="The sum of all attributes should be 40!"))
        
    #     character['attribs'] = attributes
    #     return redirect(url_for("heritage_faction"))
        
    # else:         
    #     try:
    #         ercode = f"Error: {request.args['error'] }"
    #     except:
    #         ercode = ''
        # Render template with attributes and initial values
    ercode = ''
    totpts = sum([a.value for a in attributes])
    return render_template('start_attributes.html', attributes=attributes, error=ercode, total_points=totpts)


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
