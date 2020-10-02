import csv
from datetime import datetime
import time
import requests

'''
Script created by Rafael Gomes Alves
Master's degree student at FEI University Center
This Script does the following steps inside the container
1. Open sensores.csv file
2. Load probe data for each row
3. Tries to send this data to the IoT Agent JSON
'''

# Open sensores.csv file. 
with open('sensores.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:

        # Load rpobe data for each row
        if line_count == 0:
            line_count += 1
        else:
            smr1 = row[4]
            smr2 = row[6]
            smc1 = row[5]
            smc2 = row[7]
            ah = row[2]
            at = row[3]
            st = row[8]
            lum = row[1]
            print(smr1,smr2,smc1,smc2,ah,at,st)

            # Tries to send the probe data to the Iot Agent JSON
            try:
                url = f"http://iot-agent-json:7896/iot/json?i=Probe1&k=key123"

                payload = f"{{\n \"smr1\": {smr1},\n \"smr2\":{smr2},\n \"smc1\": {smc1},\n \"smc2\": {smc2},\n \"ah\": {ah},\n \"at\": {at},\n \"st\": {st}\n,\n \"lum\": {lum}\n}}"
                headers = {
                    'content-type': 'application/json',
                    'fiware-service': 'lab',
                    'fiware-servicepath': '/'
                }

                response = requests.request("POST", url, headers=headers, data = payload)

                print(response.text.encode('utf8'))
            except:
                print(f"an error has ocurred when trying to send data in row {line_count}") # Indicate that an error has occured

            line_count += 1
            time.sleep(1800) # Wait 30 minutes to send the next data point
        print(f"Processed {line_count} lines") # Print a log with the number of lines processed 