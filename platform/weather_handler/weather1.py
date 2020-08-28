import requests
import json
from datetime import datetime
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
import time

#Create a function with what should be executed in the scheduler at the end
def get_data():
    # Get Weather Data from Open Weather map API
    url = "https://api.weather.com/v2/pws/observations/current?stationId=ISOBERNA3&format=json&units=m&apiKey=dc374a2b476948abb74a2b476968ab3b"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload).json()

    # Send Data to the entity "WeatherCurrent"
    url = "http://localhost:1026/v2/entities/WeatherCurrentWunder/attrs"

    payload = json.dumps({
        "dateObserved": {
            "value": response["observations"][0]["obsTimeLocal"],
            "type" : "Datetime"
        },
        "temperature": {
            "value": response["observations"][0]["metric"]["temp"]
        },
        "pressure": {
            "value": response["observations"][0]["metric"]["pressure"]
        },
        "windSpeed": {
            "value": response["observations"][0]["metric"]["windSpeed"]
        },
        "windDeg": {
            "value": response["observations"][0]["winddir"]
        },
        "humidity": {
            "value": response["observations"][0]["humidity"]
        },
        "precipTotal": {
            "value": response["observations"][0]["metric"]["precipTotal"]
        },  
    })

    headers = {
    'Content-Type': 'application/json',
    'fiware-service': 'lab',
    'fiware-servicepath': '/'
    }

    response = requests.request("PATCH", url, headers=headers, data = payload)

    # Get Weather Forecast for the next 5 days
    url = "https://api.weather.com/v3/wx/forecast/daily/5day?geocode=-23.73,-46.58&format=json&units=m&language=en-US&apiKey=dc374a2b476948abb74a2b476968ab3b"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload).json()
    for x in range(6):
        url = "http://localhost:1026/v2/entities/WeatherForecastWunder/attrs"

        payload = json.dumps({
            "dateForecast": {
                "value": datetime.fromtimestamp(response["validTimeUtc"][x]).isoformat()
            },
            "temperatureMax": {
                "value": response["temperatureMax"][x]
            },
            "temperatureMin": {
                "value": response["temperatureMin"][x]
            },
            "precipitation": {
                "value": response["qpf"][x]  
            }
        })
        headers = {
        'Content-Type': 'application/json',
        'fiware-service': 'lab',
        'fiware-servicepath': '/'
        }
        r = requests.request("PATCH", url, headers=headers, data = payload)
        time.sleep(2)



# Configure the scheduler to execute the function get_data each hour
scheduler = BlockingScheduler()
scheduler.add_job(get_data, 'interval', minutes=1, start_date='2020-08-25 09:00:00') #This star data should be a past time and is used to indicate that the scheduler should run in round hours lin 10,11,12 etc. 
scheduler.start() 