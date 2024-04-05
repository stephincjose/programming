from flask import Flask, render_template
import requests 
import json
from pymongo import *


app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    req = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/dublin?unitGroup=metric&key=TA8XSWUVK2M3S7GXQHHJ3349L&contentType=json')
    #req = requests.get('https://cat-fact.herokuapp.com/facts')
    #print(req.content)
    data = json.loads(req.content)

    hourly_data = []

    for hour in data['days'][0]['hours']:
        hourly_data.append({
            'datetime' : hour['datetime'],
            'datetimeEpoch': hour['datetimeEpoch'],
            'temp': hour['temp'],
            'feelslike': hour['feelslike'],
            'humidity' : hour['humidity'],
            'dew': hour['dew'],
            'precip': hour['precip'],
            'precipprob' : hour['precipprob'],
            'snow' :hour['snow'],
            'snowdepth' : hour['snowdepth'],
            'preciptype' : hour['preciptype'],
            'windgust' : hour['windgust'],
            'windspeed' : hour['windspeed'],
            'winddir' : hour['winddir'],
            'pressure' : hour['pressure'],
            'visibility' : hour['visibility'],
            'cloudcover' : hour['cloudcover'],
            'solarradiation' : hour['solarradiation'],
            'solarenergy' : hour['solarenergy'],
            'uvindex' : hour['uvindex'],
            'severerisk' : hour['severerisk'],
            'conditions' : hour['conditions'],
            'icon' : hour['icon'],
            'stations' : hour['stations'],
            'source' : hour['source']

        })
    
    temperature = data['days'][0]['temp']

    return render_template('index.html',hourly_data=hourly_data)

if __name__ == '__main__':
    app.run(port=5000,debug=True)

