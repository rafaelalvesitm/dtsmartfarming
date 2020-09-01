import csv
from datetime import datetime
import time
import requests

with open('SoilProbeData.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            smr1 = row[3]
            smr2 = row[5]
            smc1 = row[4]
            smc2 = row[6]
            ah = row[1]
            at = row[2]
            st = row[7]
            print(smr1,smr2,smc1,smc2,ah,at,st)

            try:
                url = f"http://iot-agent-json:7896/iot/json?i=Probe1&k=key123"

                payload = f"{{\n    \"smr1\": {smr1},\n    \"smr2\":{smr2},\n    \"smc1\": {smc1},\n    \"smc2\": {smc2},\n    \"ah\": {ah},\n    \"at\": {at},\n    \"st\": {st}\n}}"
                headers = {
                    'content-type': 'application/json',
                    'fiware-service': 'lab',
                    'fiware-servicepath': '/'
                }

                response = requests.request("POST", url, headers=headers, data = payload)

                print(response.text.encode('utf8'))
            except:
                print("an error has ocurred when trying to send data")
            line_count += 1
            time.sleep(1800)

    print(f"Processed {line_count} lines")