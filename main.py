from flask import Flask, render_template
import requests 
import json

app = Flask(__name__)

 
 
@app.route("/", methods=['GET'])
def index():
    req = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/dublin?unitGroup=metric&include=days%2Chours%2Calerts%2Ccurrent&key=TA8XSWUVK2M3S7GXQHHJ3349L&contentType=json')
    #req = requests.get('https://cat-fact.herokuapp.com/facts')
    #print(req.content)
    data = req.content

    return render_template('index.html',data=data)

app.run()

