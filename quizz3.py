import requests
import json
import sqlite3
key = 'fcfac1c3065489a0e4195e5e4ea9385e'
lat = 41.732
lon = 44.783
payload = {'lat': lat, 'lon':lon, 'appid':key, 'cnt':3, 'units':'metric'}
url = 'https://api.openweathermap.org/data/2.5/weather'
resp = requests.get(url, params=payload)
result = resp.json()
with open('dataa.json', 'w') as file:
    json.dump (result, file, indent=4)
status_code = resp.status_code
headers = resp.headers
temperatura = result['main']['temp']
amindi = result['weather'][0]['main']
name = result['name']
qveyana = result['sys']['country']
print(f"Temperatura: {temperatura} gradusi")
print(f"amindi: {amindi}")
print(f"Status Code: {status_code}")
print("Headers:")
for key, value in headers.items():
    print(f"{key}: {value}")
#baza
conn = sqlite3.connect('amindi.sqlite')
c = conn.cursor()
#shevqmnat cxrili romelsac gadavcemt 4 svets
c.execute('''CREATE TABLE IF NOT EXISTS weather
        (temperatura REAL,
        amindi TEXT,
        qveynis_kodi VARCHAR(50),
        lokacia VARCHAR(50))''')
#placeholderebis adgilas gadavcet 4 svetisvis mnishvnelobebi romlebic mogvaqvs json-dan
c.execute('INSERT INTO weather VALUES (?, ?, ?, ?)', (temperatura, amindi, qveyana, name))
conn.commit()
conn.close()

