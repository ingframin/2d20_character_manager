from flask import Flask, render_template, request, redirect, url_for, jsonify
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




app = Flask(__name__,template_folder='templates',static_folder='assets')
app.config["DATA_DIR"] = os.path.join(os.getcwd(), "tables")

@app.route("/")
def home():
   
    return render_template("home.html", attributes=attribs)



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
