import requests
import json

def orion(filename):
  """
    This function greets to
    the person passed in as
    a parameter
    """
  url = "localhost:1026/v2/entities/"

  with open(filename) as json_file:
    data = json.load(json_file)
    payload = json.dumps(data)
    
    headers = {
    'Content-Type': 'application/json',
    'fiware-service': 'lab',
    'fiware-servicepath': '/'
  }
  print(payload)
  response = requests.request("POST", url, headers=headers, data = payload)
  return response.text

def main():
    orion("SoilProbe1.json")

if __name__ == "__main__":
    main()