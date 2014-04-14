import os
from flask import Flask
 
app = Flask(__name__)
# Keeps Flask from swallowing error messages
app.config['PROPAGATE_EXCEPTIONS'] = True
 
@app.route("/")
def insult():
    return "Hello, code monkey!"
 
if __name__ == "__main__":
    app.run()
