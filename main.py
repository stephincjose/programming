
from flask import Flask

app = Flask(__name__)

 
 
@app.route("/")
def home():
    return f"Running Flask on Google Colab!"


@app.route("/second_page")
def home():
    return f"This is second page"

app.run()

