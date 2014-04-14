import os
from flask import Flask
import insulter
 
app = Flask(__name__)
# Keeps Flask from swallowing error messages
app.config['PROPAGATE_EXCEPTIONS'] = True
 
@app.route("/")
def insult():
    return insulter.insult() 

@app.route("/<name>")
def insult_name(name):
    return insulter.named_insult(name)
 
if __name__ == "__main__":
    app.run()
