from flask import Flask, render_template
import requests 
import json

app = Flask(__name__)

 
 
@app.route("/", methods=['GET'])
def index():
    req = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/dublin?unitGroup=metric&include=days%2Chours%2Calerts%2Ccurrent&key=TA8XSWUVK2M3S7GXQHHJ3349L&contentType=json')
    #req = requests.get('https://cat-fact.herokuapp.com/facts')
    #print(req.content)
    data = json.loads(req.content)

    hourly_data = []

    for hour in data['days'][0]['hours']:
        hourly_data.append({
            'datetime' : hour['datetime']
        })
    
    temperature = data['days'][0]['temp']

    return render_template('index.html',hourly_data=hourly_data)

app.run()

