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
collection_min_max = db['min_max']

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    req = requests.get('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/dublin?unitGroup=metric&include=days%2Chours%2Calerts%2Ccurrent&key=7NN5BGMSZ9MUZASGBLWYWK7X7&contentType=json')
    # print(req.content)
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
    
    
    try:
        # with open('json_monthly_03.txt', 'r') as file:
        #          data = json.load(file)
                          
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
            return parameters_max, parameters_min, rounded_parameters_mean

        Temperature_max, Temperature_min, Temperature_mean = findminmaxmean('Temperature_h', Temperature_h)
        Feelslike_max, Feelslike_min, Feelslike_mean = findminmaxmean('Feelslike', Feelslike_h)

        print(f"Temperature Max: {Temperature_max}, Min: {Temperature_min}, Mean: {Temperature_mean}")
        print(f"Feelslike Max: {Feelslike_max}, Min: {Feelslike_min}, Mean: {Feelslike_mean}")

        def findmean(parameter_name, parameters):
            parameters_mean = np.mean(parameters)
            rounded_parameters_mean = round(parameters_mean, 2)
            print(f'Mean {parameter_name}:', rounded_parameters_mean)
            return rounded_parameters_mean
        
    
        
        mean_Humidity=findmean('Humidity', Humidity_h) 
        mean_Dew_Dew=findmean('Dew', Dew_h)
        mean_Precip=findmean('Precip', Precip_h)
        mean_Snow=findmean('Snow', Snow_h)
        mean_Snowdepth=findmean('Snowdepth', Snowdepth_h)
        mean_Windgust=findmean('Windgust', Windgust_h)
        mean_Windspeed=findmean('Windspeed', Windspeed_h)
        mean_Winddir=findmean('Winddir', Winddir_h)
        mean_Pressure=findmean('Pressure', Pressure_h)
        mean_Visibility=findmean('Visibility', Visibility_h)
        mean_Cloudcover=findmean('Cloudcover', Cloudcover_h)
        mean_Solarradiation=findmean('Solarradiation', Solarradiation_h)
        mean_Solarenergy=findmean('Solarenergy', Solarenergy_h)
        mean_Uvindex=findmean('Uvindex', Uvindex_h)
        mean_Severerisk=findmean('Severerisk', Severerisk_h)

    #####------------------------------------------->

        datetimeEpoch= data['days'][0]['hours'][1]['datetimeEpoch']
        timezone_offset = datetime.timedelta(hours=1)  
        real_time = datetime.datetime.utcfromtimestamp(datetimeEpoch) + timezone_offset
        date = real_time.strftime('%Y-%m-%d')
        print("Real Date in GMT+1:", date)
        
        daily_parameters=[date, Temperature_max, Temperature_min, Temperature_mean,Feelslike_max, Feelslike_min, Feelslike_mean , mean_Humidity,mean_Dew_Dew,mean_Precip,mean_Snow,mean_Snowdepth,mean_Windgust,mean_Windspeed,mean_Winddir,mean_Pressure,mean_Visibility,mean_Cloudcover,mean_Solarradiation,mean_Solarenergy,mean_Uvindex,mean_Severerisk]
        # print(len(daily_parameters))
        daily_parameters_dict={'date':date, 'Temperature_max':Temperature_max, 'Temperature_min':Temperature_min, 'Temperature_mean':Temperature_mean,'Feelslike_max':Feelslike_max, 'Feelslike_min':Feelslike_min, 'Feelslike_mean':Feelslike_mean ,'mean_Humidity': mean_Humidity,'mean_Dew_Dew':mean_Dew_Dew,'mean_Precip':mean_Precip,'mean_Snow':mean_Snow,'mean_Snowdepth':mean_Snowdepth,'mean_Windgust':mean_Windgust,'mean_Windspeed':mean_Windspeed,'mean_Winddir':mean_Winddir,'mean_Pressure':mean_Pressure,'mean_Visibility':mean_Visibility,'mean_Cloudcover':mean_Cloudcover,'mean_Solarradiation':mean_Solarradiation,'mean_Solarenergy':mean_Solarenergy,'mean_Uvindex':mean_Uvindex,'mean_Severerisk':mean_Severerisk}
   
        for eachhour in range(24):
                        post = hourly_data[eachhour]
                        
                        
                        filter_datetimeEpoch = post['datetimeEpoch']
                        filter1 = {'datetimeEpoch': filter_datetimeEpoch }

                        doc1= collection.find_one({'datetimeEpoch':filter_datetimeEpoch})
                        
                        if doc1:
                            collection.replace_one(filter1,  post)
                            print('update',post)
                        else:
                            collection.insert_one(post)
                            print('inserted',post)        
                        
   
        filter_date = daily_parameters_dict['date']
        filter = {'date': filter_date }

        doc = collection_min_max.find_one({'date': filter_date })
        # print(filter_date, type(filter_date))
        
        if doc:
            collection_min_max.replace_one(filter,  daily_parameters_dict)
        else:
            collection_min_max.insert_one(daily_parameters_dict)

    except:
        print('error')
                    
    return render_template('index.html', hourly_data= hourly_data, post=post ,data=data , date=date , daily_parameters=daily_parameters)


@app.route('/view-data')
def view_data2():
    all_data = collection.find()     
    return render_template('view-data.html', all_data=all_data )

@app.route('/processed-data')
def view_data1():
    
    
    parameter_dicts = []
        
    daily_parameters_list = collection_min_max.find().sort("date", pymongo.DESCENDING)
     
    if daily_parameters_list:
        for daily_parameters_dict in daily_parameters_list:
            parameter_dicts.append(daily_parameters_dict)


    all_data = collection.find().sort("datetimeEpoch", pymongo.DESCENDING)

            
    processed_data = []

    for x in all_data:
            
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
            'Rain':'none',
            'None' :'none',
            'Snow':'none',

            'Overcast' : 'none',
            'Partially_cloudy' :'none',
            'Clear' :'none',
            'Rain' :'none'

        })
    
    for x in processed_data:
        conditions = x.get('conditions')
        if conditions:
            conditions_list = conditions.split(',')
            if 'Rain' in conditions_list:
                x['Rain'] = 'Yes'
            else:
                x['Rain'] = 'No'

            if 'Overcast' in conditions_list:
                x['Overcast'] = 'Yes'
            else:
                x['Overcast'] = 'No' 

            if 'Partially cloudy' in conditions_list:
                x['Partially_cloudy'] = 'Yes'
            else:
                x['Partially_cloudy'] = 'No'


            if 'Clear' in conditions_list:
                x['Clear'] = 'Yes'
            else:
                x['Clear'] = 'No'  
            
  


    for x in processed_data:
        if x.get('datetimeEpoch'):
            epoch_time = datetime.datetime.fromtimestamp(x.get('datetimeEpoch'))
            x['datetimeEpoch'] = epoch_time.strftime('%Y-%m-%d')

 
    for x in processed_data:
        preciptype = x.get('preciptype')
        if preciptype == ['rain']:
            x['Rain'] = 'Yes'
            x['None'] = 'No'
            x['Snow'] = 'No'


        elif preciptype is None:
            x['None'] = 'Yes'
            x['Rain'] = 'No'
            x['Snow'] = 'No'
        
        elif preciptype == ['snow']:
            x['None'] = 'No'
            x['Rain'] = 'No'
            x['Snow'] = 'Yes' 
        
    return render_template('processed-data.html', all_data=processed_data,  parameter_dicts=parameter_dicts)

if __name__ == '__main__':
    #port for local
    app.run(port=5000,debug=True)
    #port for flask
    #app.run(host='0.0.0.0', port=8080)


    