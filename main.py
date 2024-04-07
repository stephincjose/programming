from flask import Flask, render_template,jsonify
import requests 
import json
from pymongo import *
from datetime import datetime

cluster = MongoClient("")
db = cluster["test"]
collection = db["test"]

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    #req = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/dublin?unitGroup=metric&key=TA8XSWUVK2M3S7GXQHHJ3349L&contentType=json')
    ##print(req.content)
    #data = json.loads(req.content)
    try:
        with open('json_monthly_02.txt', 'r') as file:
            data = json.load(file)

        # hourly_data = []

        # for hour in data['days'][0]['hours']:
        #     hourly_data.append({
        #         'datetime' : hour['datetime'],
        #         'datetimeEpoch': hour['datetimeEpoch'],
        #         'temp': hour['temp'],
        #         'feelslike': hour['feelslike'],
        #         'humidity' : hour['humidity'],
        #         'dew': hour['dew'],
        #         'precip': hour['precip'],
        #         'precipprob' : hour['precipprob'],
        #         'snow' :hour['snow'],
        #         'snowdepth' : hour['snowdepth'],
        #         'preciptype' : hour['preciptype'],
        #         'windgust' : hour['windgust'],
        #         'windspeed' : hour['windspeed'],
        #         'winddir' : hour['winddir'],
        #         'pressure' : hour['pressure'],
        #         'visibility' : hour['visibility'],
        #         'cloudcover' : hour['cloudcover'],
        #         'solarradiation' : hour['solarradiation'],
        #         'solarenergy' : hour['solarenergy'],
        #         'uvindex' : hour['uvindex'],
        #         'severerisk' : hour['severerisk'],
        #         'conditions' : hour['conditions'],
        #         'icon' : hour['icon'],
        #         'stations' : hour['stations'],
        #         'source' : hour['source']

        #     })


        x= len(data['days'])
        
        #print(x)

        for days in range(x-1):
            hourly_data = []

            for hour in data['days'][days]['hours']:
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
                    'source' : hour['source'] })
            try:    
                for l in range(24):
                    post = hourly_data[l]
                    collection.insert_one(post)
                    #print('inserted',post)
            except:
                print('error')
    except:
        print('error')        

    return render_template('index.html', hourly_data= hourly_data)

@app.route('/view-data')


def view_data():

    pipeline = [
        {"$group": {"_id": "$datetimeEpoch", "count": {"$sum": 1}}},
        {"$match": {"count": {"$gt": 1}}}
    ] 
    duplicate_docs = list(collection.aggregate(pipeline))
    for doc in duplicate_docs:
        print(doc)
        count= doc["count"]
        for c in range(count-2):
            collection.delete_many({"datetimeEpoch": doc["_id"]})
            # print('dfdf',c)


    all_data = collection.find()     
    return render_template('view-data.html', all_data=all_data)



@app.route('/proccessed-data1')


def view_data1():
    all_data = list(collection.find())
    processed_data = []

    for x in all_data:
        cloudcover = x.get('cloudcover')
        processed_data.append({
            'datetime': x.get('datetime'),
            'datetimeEpoch': x.get('datetimeEpoch'),
            'temp': x.get('temp'),
            'feelslike': x.get('feelslike'),
            'humidity': x.get('humidity'),
            'dew': x.get('dew'),
            'precip': x.get('precip'),
            'precipprob': x.get('precipprob'),
            'snow': x.get('snow'),
            'snowdepth': x.get('snowdepth'),
            'preciptype': x.get('preciptype'),
            'windgust': x.get('windgust'),
            'windspeed': x.get('windspeed'),
            'winddir': x.get('winddir'),
            'pressure': x.get('pressure'),
            'visibility': x.get('visibility'),
            'cloudcover': x.get('cloudcover'),
            'solarradiation': x.get('solarradiation'),
            'solarenergy': x.get('solarenergy'),
            'uvindex': x.get('uvindex'),
            'severerisk': x.get('severerisk'),
            'conditions': x.get('conditions'),
        })


    for x in processed_data:
        if x.get('datetimeEpoch'):
            epoch_time = datetime.fromtimestamp(x.get('datetimeEpoch'))
            x['datetimeEpoch'] = epoch_time.strftime('%Y-%m-%d %H:%M:%S')

 
    for x in processed_data:
        preciptype = x.get('preciptype')
        if preciptype == ['rain']:
            x['preciptype'] = 'rain'
        elif preciptype is None:
            x['preciptype'] = 'None'
        
    return render_template('proccessed-data.html', all_data=processed_data)


if __name__ == '__main__':
    app.run(port=5000,debug=True)


    