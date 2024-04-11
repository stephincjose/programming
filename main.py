from flask import Flask, render_template,jsonify
import requests 
import json
from pymongo import *
from datetime import datetime
import datetime
import pymongo
import numpy as np

cluster = MongoClient("mongodb+srv://stephinjosec:passsword1@cluster0.jh2zpzm.mongodb.net/")
db = cluster["test"]
collection = db["test"]

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    req = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/dublin?unitGroup=metric&include=days%2Chours%2Calerts%2Ccurrent&key=7NN5BGMSZ9MUZASGBLWYWK7X7&contentType=json')
    print(req.content)
    data = json.loads(req.content)

    hourly_data = []
    Temperature_h=[]
    Feelslike_h=[]
    Humidity_h=[]
    Dew_h=[]
    Precip_h=[]
    Snow_h=[]
    Snowdepth_h=[]
    Windgust_h=[]
    Windspeed_h=[]
    Winddir_h=[]
    Pressure_h=[]
    Visibility_h=[]
    Cloudcover_h=[]
    Solarradiation_h=[]
    Solarenergy_h=[]
    Uvindex_h=[]
    Severerisk_h=[]
    

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
            Temperature_h.append(hour['temp'])
            Feelslike_h.append(hour['feelslike'])

            Humidity_h.append(hour['humidity'])
            Dew_h.append(hour['dew'])
            Precip_h.append(hour['precip'])
            Snow_h.append(hour['snow'])
            Snowdepth_h.append(hour['snowdepth'])
            Windgust_h.append(hour['windgust'])
            Windspeed_h.append(hour['windspeed'])
            Winddir_h.append(hour['winddir'])
            Pressure_h.append(hour['pressure'])
            Visibility_h.append(hour['visibility'])
            Cloudcover_h.append(hour['cloudcover'])
            Solarradiation_h.append(hour['solarradiation'])
            Solarenergy_h.append(hour['solarenergy'])
            Uvindex_h.append(hour['uvindex'])
            Severerisk_h.append(hour['severerisk'])




    


    def findminmaxmean(parameter_name, parameters):
        parameters_max = np.max(parameters)
        print(f'Max {parameter_name}:', parameters_max)
        parameters_min = np.min(parameters)
        print(f'Min {parameter_name}:', parameters_min)
        parameters_mean = np.mean(parameters)
        rounded_parameters_mean = round(parameters_mean, 2)
        print(f'Mean {parameter_name}:', rounded_parameters_mean)

    def findmean(parameter_name, parameters):
        parameters_mean = np.mean(parameters)
        rounded_parameters_mean = round(parameters_mean, 2)
        print(f'Mean {parameter_name}:', rounded_parameters_mean)
    
    findminmaxmean('Temperature_h', Temperature_h)
    findminmaxmean('Feelslike', Feelslike_h)

    findmean('Humidity', Humidity_h)
                    
         





    datetimeEpoch= data['days'][0]['hours'][0]['datetimeEpoch']
    timezone_offset = datetime.timedelta(hours=1)  
    real_time = datetime.datetime.utcfromtimestamp(datetimeEpoch) + timezone_offset
    date = real_time.strftime('%Y-%m-%d')
    print("Real Date in GMT+1:", date)



        

    # try:
    #     with open('json_monthly_02.txt', 'r') as file:
    #         data = json.load(file)

    #     x= len(data['days'])    
    #     #print(x)

    #     for days in range(x-1):
    #         hourly_data = []

    #         for hour in data['days'][days]['hours']:
    #             hourly_data.append({
    #                 'datetime' : hour['datetime'],
    #                 'datetimeEpoch': hour['datetimeEpoch'],
    #                 'temp': hour['temp'],
    #                 'feelslike': hour['feelslike'],
    #                 'humidity' : hour['humidity'],
    #                 'dew': hour['dew'],
    #                 'precip': hour['precip'],
    #                 'precipprob' : hour['precipprob'],
    #                 'snow' :hour['snow'],
    #                 'snowdepth' : hour['snowdepth'],
    #                 'preciptype' : hour['preciptype'],
    #                 'windgust' : hour['windgust'],
    #                 'windspeed' : hour['windspeed'],
    #                 'winddir' : hour['winddir'],
    #                 'pressure' : hour['pressure'],
    #                 'visibility' : hour['visibility'],
    #                 'cloudcover' : hour['cloudcover'],
    #                 'solarradiation' : hour['solarradiation'],
    #                 'solarenergy' : hour['solarenergy'],
    #                 'uvindex' : hour['uvindex'],
    #                 'severerisk' : hour['severerisk'],
    #                 'conditions' : hour['conditions'],
    #                 'icon' : hour['icon'],
    #                 'stations' : hour['stations'],
    #                 'source' : hour['source'] })
    #         try:    
    #             for l in range(24):
    #                 post = hourly_data[l]
    #                 collection.insert_one(post)
    #                 print('inserted',post)
    #         except:
    #             print('error')
    # except:
    #     print('error')  

    #xm = {'datetime': '11:00:00', 'datetimeEpoch': 1713002401, 'temp': 10.1, 'feelslike': 10.1, 'humidity': 71.43, 'dew': 5.1, 'precip': 0.0, 'precipprob': 12.9, 'snow': 0.0, 'snowdepth': 0.0, 'preciptype': None, 'windgust': 51.1, 'windspeed': 24.1, 'winddir': 243.9, 'pressure': 1018.7, 'visibility': 24.0, 'cloudcover': 69.1, 'solarradiation': 307.7, 'solarenergy': 1.1, 'uvindex': 3.0, 'severerisk': 10.0, 'conditions': 'Partially cloudy', 'icon': 'partly-cloudy-day', 'stations': None, 'source': 'fcst'}
    #collection.insert_one(xm)


    for l in range(24):
                    post = hourly_data[l]
                    collection.insert_one(post)
    
    


                    #print('inserted',post)
                    
    return render_template('index.html', hourly_data= hourly_data, post=post ,data=data , date=date )





@app.route('/view-data')
def view_data():
    pipeline = [
        {"$group": {"_id": "$datetimeEpoch", "count": {"$sum": 1}}},
        {"$match": {"count": {"$gt": 1}}}
    ] 
    duplicate_docs = list(collection.aggregate(pipeline))

    for doc in duplicate_docs:
        count= doc["count"]
        count_index = count
        if count > 1:
            while count_index > 1:
                #print('true')
                collection.delete_one({"datetimeEpoch": doc["_id"]})
                count_index =count_index-1
                print(count_index)

    all_data = collection.find()     
    return render_template('view-data.html', all_data=all_data,duplicate_docs= duplicate_docs )


@app.route('/processed-data')
def view_data1():
    all_data = collection.find().sort("datetimeEpoch", pymongo.DESCENDING)
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
            epoch_time = datetime.datetime.fromtimestamp(x.get('datetimeEpoch'))
            x['datetimeEpoch'] = epoch_time.strftime('%Y-%m-%d %H:%M:%S')

 
    for x in processed_data:
        preciptype = x.get('preciptype')
        if preciptype == ['rain']:
            x['preciptype'] = 'rain'
        elif preciptype is None:
            x['preciptype'] = 'None'
        
    return render_template('proccessed-data.html', all_data=processed_data)


if __name__ == '__main__':
    #port for local
    app.run(port=5000,debug=True)
    #port for flask
    #app.run(host='0.0.0.0', port=8080)


    