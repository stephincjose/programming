
from flask import Flask

app = Flask(__name__)

 
 
@app.route("/")
def home():
    return f"Running Flask on Google Colab!"

@app.route("/Second")
def home():
    return f"Second Page"



app.run()

