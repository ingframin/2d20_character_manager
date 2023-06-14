from flask import Flask, render_template, request, redirect, url_for, jsonify
from attribs import *
from factions import *
import os
import json

app = Flask(__name__,template_folder='templates',static_folder='assets')
app.config["DATA_DIR"] = os.path.join(os.getcwd(), "tables")


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/standard_generation", methods=['GET','POST'])
def standard_generation():
    return "Standard Generation"


@app.route("/points_system")
def points_system():
    # Add your code for the 12 points system here
    return "12 Points System"

@app.route("/free_character")
def free_character():
    # Add your code for the free character system here
    return "Free Character"

if __name__ == "__main__":
    # app.run(debug=True)

    import webview
    from threading import Thread
    apptr = Thread(target=app.run, kwargs={'debug':False})
    apptr.start()
    webview.create_window('Hello world', 'http://127.0.0.1:5000/',width=1000,height=650)
    webview.start()
    apptr.join()
    exit(0)       
