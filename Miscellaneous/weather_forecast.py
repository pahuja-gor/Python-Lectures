import json

import matplotlib.pyplot as plt
import requests

data = requests.get(
    "http://forecast.weather.gov/MapClick.php?lat=37.2327&lon=-80.4284&unit=0&lg=english&FcstType=json").json()
json_data = requests.get(
    "http://forecast.weather.gov/MapClick.php?lat=37.2327&lon=-80.4284&unit=0&lg=english&FcstType=json")
concise_json = json.loads(json_data.text)

print(json.dumps(concise_json, indent=2))
print(data)

list_of_temp = (data["data"]["temperature"])

list_of_temp = [int(x) for x in list_of_temp]
plt.plot(list_of_temp)
plt.xlabel("Day")
plt.ylabel("Temperature")
plt.title("The Temperature on each Day")
plt.show()
print(list_of_temp)