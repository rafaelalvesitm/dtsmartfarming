import requests
import json
import os
import time
 
time.sleep(30)

#Setup all orion entities iside orionEntities Folder

url = "http://orion:1026/v2/entities/"

files = os.listdir("orionEntities")

for (dirpath, dirnames, filenames) in os.walk("orionEntities"):
  for filename in filenames:
    with open(os.path.join(dirpath, filename)) as json_file:
      data = json.load(json_file)
      payload = json.dumps(data)
      
      headers = {
        'Content-Type': 'application/json',
        'fiware-service': 'lab',
        'fiware-servicepath': '/'
        }

      response = requests.request("POST", url, headers=headers, data = payload)
      print(response)

# Setup fiware service

url = "http://iot-agent-json:4041/iot/services"

with open("iotAgentJson/service.json") as json_file:
  data = json.load(json_file)
  payload = json.dumps(data)

headers = {
  'fiware-service': 'lab',
  'fiware-servicepath': '/',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

# Setup all soil probe devices

url = "http://iot-agent-json:4041/iot/devices"

with open("iotAgentJson/devices.json") as json_file:
  data = json.load(json_file)
  payload = json.dumps(data)
  
headers = {
  'Content-Type': 'application/json',
  'fiware-service': 'lab',
  'fiware-servicepath': '/'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

# Create a subscription for all orion entities

url = "http://orion:1026/v2/subscriptions/"

with open("subscription/subscription.json") as json_file:
  data = json.load(json_file)
  payload = json.dumps(data)

headers = {
  'Content-Type': 'application/json',
  'fiware-service': 'lab',
  'fiware-servicepath': '/'
}

response = requests.request("POST", url, headers=headers, data = payload)

print(response.text.encode('utf8'))