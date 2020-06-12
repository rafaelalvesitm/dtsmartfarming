import requests
import time
import random

time.sleep(120)
# Create Orion Entity
try:
  url = "http://orion:1026/v2/entities/"

  payload = "{\n    \"id\": \"urn:ngsi-ld:SoilProbe:001\",\n    \"type\": \"SoilProbe\",\n    \"name\": {\n        \"type\": \"Text\",\n        \"value\": \"3 depth soil probe\"\n    },\n    \"location\": {\n        \"type\": \"geo:json\",\n        \"value\": {\n            \"type\": \"Point\",\n            \"coordinates\": [\n                13.3986,\n                52.5547\n            ]\n        }\n    },\n    \"manufacturer\": {\n        \"type\": \"Text\",\n        \"value\": \"Centro Universitário FEI\"\n    },\n    \"numberOfSensors\": {\n        \"type\": \"Number\",\n        \"value\": \"3\"\n    },\n    \"soilMoistureRawDepth1\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"soilMoistureRawDepth2\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"soilMoistureCalibratedDepth1\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"soilMoistureCalibratedDepth2\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"airHumidity\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"airTemperature\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"soilTemperature\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"refManagementZone\": {\n        \"type\": \"Relationship\",\n        \"value\": \"urn:ngsi-ld:ManagementZone:001\"\n    }\n}"
  headers = {
    'Content-Type': 'application/json',
    'fiware-service': 'lab',
    'fiware-servicepath': '/'
  }

  response = requests.request("POST", url, headers=headers, data = payload)
except:
  print("http://orion:1026/v2/entities/ not worked")

try:
  url = "http://localhost:1026/v2/entities/"

  payload = "{\n    \"id\": \"urn:ngsi-ld:SoilProbe:001\",\n    \"type\": \"SoilProbe\",\n    \"name\": {\n        \"type\": \"Text\",\n        \"value\": \"3 depth soil probe\"\n    },\n    \"location\": {\n        \"type\": \"geo:json\",\n        \"value\": {\n            \"type\": \"Point\",\n            \"coordinates\": [\n                13.3986,\n                52.5547\n            ]\n        }\n    },\n    \"manufacturer\": {\n        \"type\": \"Text\",\n        \"value\": \"Centro Universitário FEI\"\n    },\n    \"numberOfSensors\": {\n        \"type\": \"Number\",\n        \"value\": \"3\"\n    },\n    \"soilMoistureRawDepth1\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"soilMoistureRawDepth2\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"soilMoistureCalibratedDepth1\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"soilMoistureCalibratedDepth2\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"airHumidity\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"airTemperature\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"soilTemperature\": {\n        \"type\": \"number\",\n        \"value\": \"\"\n    },\n    \"refManagementZone\": {\n        \"type\": \"Relationship\",\n        \"value\": \"urn:ngsi-ld:ManagementZone:001\"\n    }\n}"
  headers = {
    'Content-Type': 'application/json',
    'fiware-service': 'lab',
    'fiware-servicepath': '/'
  }

  response = requests.request("POST", url, headers=headers, data = payload)
except:
  print("http://localhost:1026/v2/entities/ not worked")


print("what just happened?")