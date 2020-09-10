import requests
import time
import random
from apscheduler.schedulers.blocking import BlockingScheduler
import pymysql
import json
from datetime import date
from datetime import datetime

''' Developed by Rafael Gomes Alves
This script is used inside the irrigationRecommendation container and does the following:
1. Get weather parameters and sent it to the referenceEvapotranspiration Entity
2. Calculate Reference evaotranspiration for the city of São Bernardo do Cmapo, São Paulo, Brazil
3. Calculate the irrigation recommendation based on FAO's Crop Evapotranspiration
4. Calculate the irrigation recommendation based on a Fuzzy Inference System developed by Gilberto Souza
'''


def get_daily_info():
  """ 
  Colled daily weather data and calculate max, min, avg values for temperature, relative humidity and wind speed
  """
  connection = pymysql.connect(host='db-mysql', user='root', password='123', db='lab')

  # Select Maximum daily temperature
  cursor = connection.cursor()
  sql = 'SELECT MAX(CASE attrName WHEN "temperature" THEN attrValue END) FROM `WeatherCurrent_WeatherCurrent` WHERE date(recvTime) = curdate()'
  cursor.execute(sql)
  tmax = cursor.fetchone()

  # Collect minimum daily temperature
  sql = 'SELECT MIN(CASE attrName WHEN "temperature" THEN attrValue END) FROM `WeatherCurrent_WeatherCurrent` WHERE date(recvTime) = curdate()'
  cursor.execute(sql)
  tmin = cursor.fetchone()

  # Collect minimum daily temperature
  sql = 'SELECT AVG(CASE attrName WHEN "temperature" THEN attrValue END) FROM `WeatherCurrent_WeatherCurrent` WHERE date(recvTime) = curdate()'
  cursor.execute(sql)
  tmed = cursor.fetchone()

  # Collect maximum daily humidity
  sql = 'SELECT MAX(CASE attrName WHEN "humidity" THEN attrValue END) FROM `WeatherCurrent_WeatherCurrent` WHERE date(recvTime) = curdate()'
  cursor.execute(sql)
  rhmax = cursor.fetchone()

  # Collect minimum daily humidity
  sql = 'SELECT MIN(CASE attrName WHEN "humidity" THEN attrValue END) FROM `WeatherCurrent_WeatherCurrent` WHERE date(recvTime) = curdate()'
  cursor.execute(sql)
  rhmin = cursor.fetchone()

  # Collect average daily humidity
  sql = 'SELECT AVG(CASE attrName WHEN "humidity" THEN attrValue END) FROM `WeatherCurrent_WeatherCurrent` WHERE date(recvTime) = curdate()'
  cursor.execute(sql)
  rhmed = cursor.fetchone()

  # Collect average daily wind speed
  sql = 'SELECT MAX(CASE attrName WHEN "windSpeed" THEN attrValue END) FROM `WeatherCurrent_WeatherCurrent` WHERE date(recvTime) = curdate()'
  cursor.execute(sql)
  vmax = cursor.fetchone()

  # Collect average daily wind speed
  sql = 'SELECT MIN(CASE attrName WHEN "windSpeed" THEN attrValue END) FROM `WeatherCurrent_WeatherCurrent` WHERE date(recvTime) = curdate()'
  cursor.execute(sql)
  vmin = cursor.fetchone()

  # Collect average daily wind speed
  sql = 'SELECT AVG(CASE attrName WHEN "windSpeed" THEN attrValue END) FROM `WeatherCurrent_WeatherCurrent` WHERE date(recvTime) = curdate()'
  cursor.execute(sql)
  vmed = cursor.fetchone()

  payload = json.dumps({
      "dateObserved": {
          "value": datetime.now().isoformat()
      },
      "dailyTmax": {
          "value": float(tmax[0])
      },
      "dailyTmin": {
          "value": float(tmin[0])
      },
      "dailyTmed": {
          "value": float(tmed[0])
      },
      "dailyRhmax": {
          "value": float(rhmax[0])
      },
      "dailyRhmin": {
          "value": float(rhmin[0])
      },
      "dailyRhmed": {
          "value": float(rhmed[0])
      },
      "dailyVmax": {
          "value": float(vmax[0])
      },
      "dailyVmin": {
          "value": float(vmin[0])
      },
      "dailyVmed": {
          "value": float(vmed[0])
      }
  })

  print(f'Sending payload to Orion: {payload}')

  url = "http://orion:1026/v2/entities/urn:ngsi-ld:referenceEvapotranspiration:1/attrs"

  headers = {
      'Content-Type': 'application/json',
      'fiware-service': 'lab',
      'fiware-servicepath': '/'
      }

  try:
    response = requests.request("PATCH", url, headers=headers, data = payload)
    print(response.text.encode('utf8'))
  except requests.exceptions.RequestException as e:  # This is the correct syntax
    print(e)
    

scheduler = BlockingScheduler()
scheduler.add_job(get_daily_info, 'interval', minutes=0.5)
scheduler.start()