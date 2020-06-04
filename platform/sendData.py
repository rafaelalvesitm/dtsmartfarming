import requests
import random
import time

while True:
    time.sleep(5)


    url = "http://127.0.0.1:7896/iot/json?i=Probe001&k=key123"

    payload = "{\n    \"smr1\": %d,\n    \"smr2\": %d,\n    \"smr3\": %d\n}" % (random.randint(10,30), random.randint(10,30),random.randint(10,30) )
    headers = {
        'content-type': 'application/json',
        'fiware-service': 'lab',
        'fiware-servicepath': '/'
    }
    print("Sendind measurements")
    response = requests.request("POST", url, headers=headers, data = payload)

    print(response.text.encode('utf8'))