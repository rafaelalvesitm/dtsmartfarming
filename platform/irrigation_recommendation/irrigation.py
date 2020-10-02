import datetime
from datetime import date
from datetime import datetime
import requests
import pymysql
import json
import math
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import numpy as np
import matplotlib
from apscheduler.schedulers.blocking import BlockingScheduler
import config

''' Developed by Rafael Gomes Alves
This script is used inside the irrigationRecommendation container and does the following:
1. Get weather parameters and sent it to the referenceEvapotranspiration Entity
2. Calculate Reference evaotranspiration for the city of São Bernardo do Campo, São Paulo, Brazil
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

def evapotranspiration():
    ''' Calculates the reference evapotranspiration based on referenceEvapotranspiration the entity and Sunrise and sunset hours
    1. Gets data from the reference Evapotranspiration entity. 
    2. Gets Sunrise and Sunsset hours from the OpenWeather API
    3. Calculates the reference evapotranspiration. 
    4. Send the daily evapotranspiration to the reference Evapotranspiration Entity. 
    '''
    url = "http://orion:1026/v2/entities/urn:ngsi-ld:referenceEvapotranspiration:1/attrs?options=keyValues"

    payload = {}
    headers = {
    'fiware-service': 'lab',
    'fiware-servicepath': '/'
    }

    response = requests.request("GET", url, headers=headers, data = payload).json()

    day_corr = date.today().toordinal() - date(date.today().year,1,1).toordinal()
    tmax = response['dailyTmax']
    tmin = response['dailyTmin']
    tmed = response['dailyTmed']
    rhmax = response['dailyRhmax']
    v_med = response['dailyVmed']
    alt_v = 2
    rhmed =response['dailyRhmed']

    # Collect sunrise and sunset hours from Ope Weather API and calculate difference
    url = "http://api.openweathermap.org/data/2.5/weather?id=3449344&appid=1b43995d45e76484eac79c54b28ad885&units=metric"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    r = response.json()
    n = datetime.fromtimestamp(r['sys']['sunset']) - datetime.fromtimestamp(r['sys']['sunrise'])
    n = n.total_seconds()/3600


    # tmax is maximum temperature for the day
    # tmin is the minimum temperature for the day
    # rhmax is the maximum relative humidity for the day
    # n is the actual duration of sunshine [hour]
    # v_med is the average wind velocity Km/h
    # alt_v is the altitute from the ground that the wind speed is collected. As for a weather station for example. 
    # rhmed

    # day_corr is the current date in the range 1 to 365
    elev = 801 # Elevation from sea level. Used the city of São Bernardo- São Paulo - Brazil. Change if needed. 
    p = 92.183188 # Atmospheric Pressure use eq 101.3*math.pow((293-0.0065*elev)/293,5.26). Used the city of São Bernardo- São Paulo - Brazil. Change if needed. 
    phi = -0,414081215084 # latitude in radians.  Used the city of São Bernardo- São Paulo - Brazil. Change if needed.
    y = 0.665*math.pow(10,-3)*p # y is the psycometric constant
    dr = 1 + 0.033*math.cos((2*math.pi*day_corr)/365) # Dr is Relative Distance Earth-Sun
    delt = 0.409 * math.sin(((2*math.pi*day_corr)/365)-1.39) # Delt is solar declination
    e0_tmax = 0.6108*math.pow(math.e,((17.27*tmax)/(tmax+237.3))) # eo_tmax is saturation vapor pressure for the max air temperature
    e0_tmin = 0.6108*math.pow(math.e,((17.27*tmin)/(tmin+237.3))) # eo_tmin is saturation vapor pressure for the min air temperature
    es = (e0_tmax + e0_tmin)/2 # es is the mean saturation vapor pressure
    D = (4098*(0.6108*math.pow(math.e,((17.27*tmed)/(tmed+237.3)))))/math.pow((tmed+237.3),2) # D is Slope Vapor Pressure Curve
    ea = es*rhmed/100 # ea us actual vapor pressure considering an average relative humidity 
    ws = math.acos(-math.tan(phi)*math.tan(delt)) #Ws is sunset hour angle
    ra = 37.5860314*dr*((ws*math.sin(phi)*math.sin(delt)) + (math.cos(phi)*math.cos(delt)*math.sin(ws))) # Ra is Extraterrestrial Radiation
    rs = (0.25 + (0.5 * (n/(7.6394 * ws))))*ra #*0.408 Rs is solar radiation 
    rns = 0.77*rs #rns ius Net Shortwave Radiation
    rso = (0.75*ra) # Rso is Clear Sky Solar Radiation
    f_rs_rso = rs/rso
    if f_rs_rso > 1:
        f_rs_rso = 1
    rnl = (4.903*math.pow(10,-9)) * ((math.pow((tmax+273.16),4) + math.pow((tmin+273.16),4))/2) * (0.34+(-0.14*math.sqrt(ea))) *  ((1.35*(f_rs_rso))-0.35) # Rnl is Net Long Wave Radiation
    r_n = rns - rnl # Rn is Neet Radiation
    g = 0
    uz = v_med*1000/3600 # uz is Wind Speed measured at Z height in m/s
    u2 = uz*(4.87/(math.log(67.8*alt_v - 5.42))) #u2 is is wind speed at 2m above ground
    et_o = ((0.408*D*(r_n-g)+y*(900/(tmed+273))*u2*(es-ea))/(D+y*(1+0.34*u2)))/0.85 # Calculate daily evapotranspiration based on the values before

    payload = json.dumps({
        "evapotranspiration": {
            "value": et_o
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

def fao_recommendation():
    ''' Calculate Fao's irrigation recommendation for a crop of Pepper and send to management zone 1
    1. Get daily reference evapotranspiration (Eto) from referenceEvappotranspiration entity
    2. Get days after seeding (Das) from cropInstance evapotranspiration
    3. Get crop Koeficiente (kc) from Crop type entity
    4. Send irrigation recommendation based on Eto * Kc
    '''

    # 1. Get daily reference evapotranspiration (Eto) from referenceEvappotranspiration entity
    url = "http://orion:1026/v2/entities/urn:ngsi-ld:referenceEvapotranspiration:1/attrs?options=keyValues"

    payload = {}
    headers = {
    'fiware-service': 'lab',
    'fiware-servicepath': '/'
    }
    response = requests.request("GET", url, headers=headers, data = payload).json()
    eto = response['evapotranspiration']

    # 2. Get days after seeding (Das) from cropInstance evapotranspiration
    url = "http://orion:1026/v2/entities/urn:ngsi-ld:CropInstance:Pepper/attrs?options=keyValues"
    payload = {}
    headers = {
    'fiware-service': 'lab',
    'fiware-servicepath': '/'
    }
    response = requests.request("GET", url, headers=headers, data = payload).json()
    das = date.today().toordinal() - datetime.strptime(response['SeedingDay'], '%Y-%m-%dT%H:%M:%S.%fZ').toordinal()

    # 3. Get crop Koeficiente (kc) from Crop type entity
    url = "http://orion:1026/v2/entities/urn:ngsi-ld:CropType:Pepper/attrs?options=keyValues"
    payload = {}
    headers = {
    'fiware-service': 'lab',
    'fiware-servicepath': '/'
    }
    r = requests.request("GET", url, headers=headers, data = payload).json()
    kc = 0
    IniDays = float(r['stageIniDays'])
    DevDays = float(r['stageDevDays'])
    MidDays = float(r['stageMidDays'])
    LateDays = float(r['stageLateDays'])
    IniKc = float(r['stageIniKc'])
    MidKc = float(r['stageMidKc'])
    LateKc = float(r['stageLateKc'])

    if das <= IniDays:
        kc = IniKc
    elif das > IniDays and das <= IniDays + DevDays:
        kc = IniKc + ((MidKc-IniKc) * (das - IniDays)) / (DevDays)
    elif das > IniDays + DevDays and das <= IniDays + DevDays + MidDays:
        kc = MidKc
    elif das > IniDays + DevDays + MidDays and das <= IniDays + DevDays + MidDays + LateDays:
        kc = LateKc + ((MidKc - LateKc) * (IniDays + DevDays + MidDays + LateDays - das)) / (LateDays)
    else:
        print('error')

    # 4. Send irrigation recommendation based on Eto * Kc
    payload = json.dumps({
        "irrigationInMilimiters": {
            "value": eto*kc
        }
    })

    print(f'Sending payload to Orion: {payload}')

    url = "http://orion:1026/v2/entities/urn:ngsi-ld:IrrigationRecommendation:1/attrs"

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
    
def fuzzy_recommendation():
    ''' Calculate Fuzzy Irrigation recommendation for a crop of Pepper and send to management zone 2
    1. Get daily reference evapotranspiration (Eto) from referenceEvappotranspiration entity
    2. Get days after seeding (Das) from cropInstance evapotranspiration
    3. Get crop Coeficiente (kc) from Crop type entity
    4. Get rain prediction and rain probability for the next day from Weather Forecast Entity.
    5. Get Daily Average Reading for the Soil Probe
    5. Send irrigation recommendation based on Eto * Kc
    '''


    # 1. Get daily reference evapotranspiration (Eto) from referenceEvappotranspiration 2 entity
    url = "http://orion:1026/v2/entities/urn:ngsi-ld:referenceEvapotranspiration:1/attrs?options=keyValues"

    payload = {}
    headers = {
    'fiware-service': 'lab',
    'fiware-servicepath': '/'
    }
    response = requests.request("GET", url, headers=headers, data = payload).json()
    eto = float(response['evapotranspiration'])


    # 2. Get days after seeding (Das) from cropInstance evapotranspiration
    url = "http://orion:1026/v2/entities/urn:ngsi-ld:CropInstance:Pepper/attrs?options=keyValues"
    payload = {}
    headers = {
    'fiware-service': 'lab',
    'fiware-servicepath': '/'
    }
    response = requests.request("GET", url, headers=headers, data = payload).json()
    das_in = date.today().toordinal() - datetime.strptime(response['SeedingDay'], '%Y-%m-%dT%H:%M:%S.%fZ').toordinal()

    # 3. Get crop Koeficiente (kc) from Crop type entity
    url = "http://orion:1026/v2/entities/urn:ngsi-ld:CropType:Pepper/attrs?options=keyValues"
    payload = {}
    headers = {
    'fiware-service': 'lab',
    'fiware-servicepath': '/'
    }
    r = requests.request("GET", url, headers=headers, data = payload).json()

    kc = 0
    IniDays = float(r['stageIniDays'])
    DevDays = float(r['stageDevDays'])
    MidDays = float(r['stageMidDays'])
    LateDays = float(r['stageLateDays'])
    IniKc = float(r['stageIniKc'])
    MidKc = float(r['stageMidKc'])
    LateKc = float(r['stageLateKc'])

    if das_in <= IniDays:
        kc = IniKc
    elif das_in > IniDays and das_in <= IniDays + DevDays:
        kc = IniKc + ((MidKc-IniKc) * (das_in - IniDays)) / (DevDays)
    elif das_in > IniDays + DevDays and das_in <= IniDays + DevDays + MidDays:
        kc = MidKc
    elif das_in > IniDays + DevDays + MidDays and das_in <= IniDays + DevDays + MidDays + LateDays:
        kc = LateKc + ((MidKc - LateKc) * (IniDays + DevDays + MidDays + LateDays - das_in)) / (LateDays)
    else:
        print('error')

    # 4. Get rain prediction and rain probability for the next day from Weather Forecast Entity.

    url = f"https://api.openweathermap.org/data/2.5/onecall?lat=-23.73&lon=-46.58&exclude=minutely,hourly&appid={config.api_key}&units=metric"
    payload = {}
    headers= {}
    r = requests.request("GET", url, headers=headers, data = payload).json()

    rain_prob_in = r["daily"][1]["pop"]

    rain_pred = 0
    if "rain" in r["daily"][1].keys():
        rain_pred_in = r["daily"][1]["rain"]
    else:
        rain_pred_in= 0

    # 5. Get Average sensor reading for both soil moisture sensors

    connection = pymysql.connect(host='db-mysql', user='root', password='123', db='lab')
    cursor = connection.cursor()
    sql = 'SELECT AVG(CASE attrName WHEN "soilMoistureCalibratedDepth1" THEN attrValue END) FROM `urn_ngsi-ld_SoilProbe_1_SoilProbe` WHERE date(recvTime) = curdate()'
    cursor.execute(sql)
    sm1 = cursor.fetchone()
    avg_soil_moisture_1 = float(sm1[0])

    sql = 'SELECT AVG(CASE attrName WHEN "soilMoistureCalibratedDepth2" THEN attrValue END) FROM `urn_ngsi-ld_SoilProbe_1_SoilProbe` WHERE date(recvTime) = curdate()'
    cursor.execute(sql)
    sm2 = cursor.fetchone()
    avg_soil_moisture_2 = float(sm1[0])

    # 6. Get daily arverage rain for the current day/month

    url = "http://orion:1026/v2/entities/urn:ngsi-ld:rainAvg:SBC/attrs?options=keyValues"
    payload = {}
    headers = {
    'fiware-service': 'lab',
    'fiware-servicepath': '/'
    }
    r = requests.request("GET", url, headers=headers, data = payload).json()

    month = datetime.now().strftime('%h')

    daily_rain_avg = float(r[month])

    # Dynamic rain forecast levels based on daily average rain for the current month for fuzzifier input.
    ini = round(daily_rain_avg * 0.25,0)
    med = round(daily_rain_avg * 1.0,0)
    fin = round(daily_rain_avg * 1.75,0)

    # Define Variables
    das = ctrl.Antecedent(np.arange(0, 110, 0.25), 'das') # Das = Days after seeding
    rain_pred = ctrl.Antecedent(np.arange(0, 5, 0.25), 'rain_pred') # rain_pred = Rain prediction in mm
    rain_prob = ctrl.Antecedent(np.arange(0, 100, 0.25), 'rain_prob') # rain_prob = rain_ probability in %
    depl = ctrl.Antecedent(np.arange(18, 36, 0.25), 'depl') # Depl = Depletion point in %
    evapo = ctrl.Antecedent(np.arange(0, 10, 0.25), 'evapo') # Evapo = Crop Evapotranspiration Etc
    irrig = ctrl.Consequent(np.arange(0, 31, 0.25), 'irrig') # irrig = irrigation in mm

    # Define functions for the rain probability
    rain_prob['minimum'] = fuzz.trimf(rain_prob.universe, [0, 0, 25])
    rain_prob['low'] = fuzz.trimf(rain_prob.universe, [0, 25, 50])
    rain_prob['medium'] = fuzz.trimf(rain_prob.universe, [25, 50, 75])
    rain_prob['high'] = fuzz.trimf(rain_prob.universe, [50, 75, 100])
    rain_prob['very high'] = fuzz.trimf(rain_prob.universe, [75, 100, 3000])

    # Define functions for days after seeding
    das['emergency'] = fuzz.trimf(das.universe, [0, 0, 15])
    das['normal'] = fuzz.trimf(das.universe, [0, 15, 65])
    das['flattening'] = fuzz.trimf(das.universe, [60, 65, 70])
    das['final'] = fuzz.trimf(das.universe, [65, 70, 3000])

    # Define functions for the crop revapotranspiration
    evapo['low'] = fuzz.trimf(evapo.universe, [0, 0, 5])
    evapo['medium'] = fuzz.trimf(evapo.universe, [3, 5, 7])
    evapo['high'] = fuzz.trimf(evapo.universe, [5, 7, 9])
    evapo['very high'] = fuzz.trimf(evapo.universe, [7, 9, 3000])

    # Define functions for rain prediction in comparison with ETc Meand rain_pre = Rain predicition/Eto
    rain_pred['low'] = fuzz.trimf(rain_pred.universe, [0, 0, med])
    rain_pred['ideal'] = fuzz.trimf(rain_pred.universe, [ini, med, fin])
    rain_pred['high'] = fuzz.trimf(rain_pred.universe, [med, fin, 3000])

    # Define functions for the depletion point. Defined based on wilting point and Field Capacity
    depl['critical'] = fuzz.trimf(depl.universe, [13, 13, 17.4])
    depl['low'] = fuzz.trimf(depl.universe, [13, 17.4, 21.8])
    depl['ideal'] = fuzz.trimf(depl.universe, [17.4, 21.8, 26.2])
    depl['high'] = fuzz.trimf(depl.universe, [21.8, 26.2, 35])
    depl['very high'] = fuzz.trimf(depl.universe, [26.2, 35, 1000])

    # Define functions for the irrigation recommendation
    irrig['minimum'] = fuzz.trimf(irrig.universe, [0, 0, 2])
    irrig['low'] = fuzz.trimf(irrig.universe, [0, 2, 4])
    irrig['ideal'] = fuzz.trimf(irrig.universe, [2, 4, 6])
    irrig['high'] = fuzz.trimf(irrig.universe, [4, 6, 8])
    irrig['very high'] = fuzz.trimf(irrig.universe, [6, 8, 20])

    # Define fuzzy inference rules
    rule_1 = ctrl.Rule(depl['critical'], irrig['very high'])
    rule_2 = ctrl.Rule(depl['very high'] & (das['final'] | das['normal']), irrig['minimum'])
    rule_3 = ctrl.Rule(depl['low'] & (rain_pred['low'] | rain_pred['ideal']) & rain_prob['low'] & (evapo['high'] | evapo['very high']), irrig['very high'])
    rule_31 = ctrl.Rule(depl['low'] & (rain_pred['low'] | rain_pred['ideal']) & rain_prob['low'] & (evapo['medium'] | evapo['high']), irrig['ideal'])
    rule_4 = ctrl.Rule(depl['low'] & (rain_pred['ideal'] | rain_pred['high']) & (rain_prob['medium'] | rain_prob['high']) & (evapo['high'] | evapo['medium']), irrig['ideal'])
    rule_5 = ctrl.Rule(depl['low'] & rain_pred['high'] & (rain_prob['medium'] | rain_prob['high']| rain_prob['very high']) & (evapo['low'] | evapo['medium']), irrig['low'])
    rule_6 = ctrl.Rule(depl['ideal'] & (rain_pred['low'] | rain_pred['ideal']) & (rain_prob['low'] | rain_prob['medium']) & (evapo['very high'] | evapo['high'] | evapo['medium']), irrig['low'])
    rule_7 = ctrl.Rule(depl['ideal'] & (rain_pred['ideal'] | rain_pred['high']) & (rain_prob['medium'] | rain_prob['high'] | rain_prob['very high']) & (evapo['low'] | evapo['medium']), irrig['low'])
    rule_8 = ctrl.Rule(depl['high'] & rain_pred['low'] & (rain_prob['low'] | rain_prob['medium'] | rain_prob['high']), irrig['ideal'])
    rule_9 = ctrl.Rule(depl['high'] & (rain_pred['ideal'] | rain_pred['high']) & (rain_prob['low'] | rain_prob['low'] | rain_prob['medium'] | rain_prob['high'] | rain_prob['very high']), irrig['minimum'])
    rule_10 = ctrl.Rule((das['emergency'] | das['flattening']) & (depl['low'] | depl['ideal']), irrig['high'])
    rule_11 = ctrl.Rule(depl['very high'], irrig['low'])
    rule_12 = ctrl.Rule(depl['ideal'], irrig['ideal'])
    rule_13 = ctrl.Rule(depl['high'], irrig['low'])
    rule_14 = ctrl.Rule(depl['high'] & das['final'], irrig['low'])


    # Define fuzzy inference system
    out_crl = ctrl.ControlSystem([rule_31, rule_14, rule_12, rule_13, rule_1, rule_2, rule_3, rule_4, rule_5, rule_6, rule_7, rule_8, rule_9, rule_10, rule_11])

    # Define fuzzy input variables values
    fuzzy = ctrl.ControlSystemSimulation(out_crl)
    fuzzy.input['das'] = das_in
    fuzzy.input['rain_pred'] = rain_pred_in
    fuzzy.input['rain_prob'] = rain_prob_in
    fuzzy.input['depl'] = (avg_soil_moisture_1 * avg_soil_moisture_2) / 2
    fuzzy.input['evapo'] = eto * kc

    # Compute and define daily irrigation recommendation
    fuzzy.compute()
    daily_irrig = (round((fuzzy.output['irrig']), 1))

    # 6. Send irrigation recommendation to the management zone 2
    payload = json.dumps({
        "irrigationInMilimiters": {
            "value": daily_irrig,
            "type": "Float"
        }
    })

    print(f'Sending payload to Orion: {payload}')

    url = "http://orion:1026/v2/entities/urn:ngsi-ld:IrrigationRecommendation:2/attrs"

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
scheduler.add_job(get_daily_info, 'interval', minutes=5, start_date='2020-09-25 09:00:00')
scheduler.add_job(evapotranspiration, 'interval', minutes=5, start_date='2020-09-25 09:01:00')
scheduler.add_job(fao_recommendation, 'interval', minutes=5, start_date='2020-09-25 09:2:00')
scheduler.add_job(fuzzy_recommendation, 'interval', minutes=5, start_date='2020-09-25 09:3:00')

scheduler.start()