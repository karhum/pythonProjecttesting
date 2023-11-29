import json
import urllib.request
url = "https://edu.frostbit.fi/api/weather/"
req = urllib.request.Request(url)
raw_data = urllib.request.urlopen(req).read().decode("UTF-8")
weather = json.loads(raw_data)

weak_wind = weather[0]["wind"]
strong_wind = 0

weak_wind_location = weather[0]["location"]
strong_wind_location = ""

for wind in weather:
    if wind['wind'] < weak_wind or weak_wind == 0:
        weak_wind = wind['wind']
        weak_wind_location = wind['location']

for wind in weather:
    if wind['wind'] > strong_wind:
        strong_wind = wind['wind']
        strong_wind_location = wind['location']

location = weather[0]

print(f"Strongest wind today at location: {strong_wind_location}, {strong_wind} m/s")
print(f"Weakest wind today at location: {weak_wind_location}, {weak_wind} m/s")
