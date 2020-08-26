import requests
import json
from datetime import datetime
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler

#Create a function with what should be executed in the scheduler at the end
def get_data():
    # Get Weather Data from Open Weather map API
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=-23.73&lon=-46.58&exclude=minutely,hourly&appid=1b43995d45e76484eac79c54b28ad885&units=metric"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    r = response.json()

    # Send Data to the entity "WeatherCurrent"
    url = "http://orion:1026/v2/entities/WeatherCurrent/attrs"

    payload = json.dumps({
        "dateObserved": {
            "value": datetime.fromtimestamp(r["current"]["dt"]).isoformat(),
            "type" : "Datetime"
        },
        "temperature": {
            "value": r["current"]["temp"]
        },
        "pressure": {
            "value": r["current"]["pressure"]
        },
        "windSpeed": {
            "value": r["current"]["wind_speed"]
        },
        "windDeg": {
            "value": r["current"]["wind_deg"]
        },
        "humidity": {
            "value": r["current"]["humidity"]
        }
    })

    headers = {
    'Content-Type': 'application/json',
    'fiware-service': 'lab',
    'fiware-servicepath': '/'
    }

    response = requests.request("PATCH", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))

    # Loop Thought each daily forecast for the next seven days
    for daily in r["daily"]:
        #print(datetime.fromtimestamp(daily["dt"]).isoformat(), daily["temp"]["max"], daily["temp"]["min"], daily["pressure"], daily["humidity"], daily["wind_speed"], daily["wind_deg"], daily["pop"])
        
        # Send Data to the entity "WeatherCurrent"
        url = "http://orion:1026/v2/entities/WeatherForecast/attrs"

        payload = json.dumps({
            "dateForecast": {
                "value": datetime.fromtimestamp(daily["dt"]).isoformat(),
                "type" : "Datetime"
            },
            "probability": {
                "value":  daily["pop"]
            },
            "temperatureMax": {
                "value": daily["temp"]["max"]
            },
            "temperatureMin": {
                "value": daily["temp"]["min"]
            },
            "pressure": {
                "value": daily["pressure"]
            },
            "windSpeed": {
                "value": daily["wind_speed"]
            },
            "windDeg": {
                "value": daily["wind_deg"]
            },
            "humidity": {
                "value": daily["humidity"]
            }
        })

        headers = {
        'Content-Type': 'application/json',
        'fiware-service': 'lab',
        'fiware-servicepath': '/'
        }

        response = requests.request("PATCH", url, headers=headers, data = payload)

        print(response.text.encode('utf8'))


# Configure the scheduler to execute the function get_data each hour
scheduler = BlockingScheduler()
scheduler.add_job(get_data, 'interval', minutes=1, start_date='2020-08-25 09:00:00') #This star data should be a past time and is used to indicate that the scheduler should run in round hours lin 10,11,12 etc. 
scheduler.start() 