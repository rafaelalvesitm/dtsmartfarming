import requests
import json
from datetime import datetime
import pytz
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import config

#Create a function with what should be executed in the scheduler at the end
def get_openweather():
    # Get Weather Data from Open Weather map API
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat=-23.73&lon=-46.58&exclude=minutely,hourly&appid={config.api_key}&units=metric"
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
        rain = 0
        if "rain" in daily.keys():
            rain= daily["rain"]
        else:
            rain = 0

        time.sleep(2)
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
            "rain": {
                "value":  rain
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

#Create a function with what should be executed in the scheduler at the end
def get_wunder():
    # Get Weather Data from Open Weather map API
    url = f"https://api.weather.com/v2/pws/observations/current?stationId=ISOBERNA3&format=json&units=m&apiKey={config.api_key_wunder}"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload).json()

    # Send Data to the entity "WeatherCurrent"
    url = "http://orion:1026/v2/entities/WeatherCurrentWunder/attrs"

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
    url = f"https://api.weather.com/v3/wx/forecast/daily/5day?geocode=-23.73,-46.58&format=json&units=m&language=en-US&apiKey={config.api_key_wunder}"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload).json()
    for x in range(6):
        url = "http://orion:1026/v2/entities/WeatherForecastWunder/attrs"

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
scheduler.add_job(get_openweather, 'interval', minutes=1, start_date='2020-08-25 09:00:00') #This star data should be a past time and is used to indicate that the scheduler should run in round hours lin 10,11,12 etc. 
scheduler.add_job(get_wunder, "interval", minutes = 1, start_date = "2020-08-25 09:00:00")
scheduler.start() 