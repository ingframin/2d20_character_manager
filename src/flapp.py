from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import json

app = Flask(__name__,template_folder='templates',static_folder='assets')
app.config["DATA_DIR"] = os.path.join(os.getcwd(), "tables")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/standard_generation", methods=['GET','POST'])
def standard_generation():
    if request.method == 'POST':
        update_session(request.get_data())
    else:

        with open('./tables/attributes.json') as f:
            attributes = json.load(f)
        # Set initial values for attributes
        for attribute in attributes:
            attribute['current_value'] = attribute['value']
        
        # Render template with attributes and initial values
        return render_template('start_attributes.html', attributes=attributes)


def update_session(data):
    print(data)

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
