import requests
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np

response = requests.get("https://think.cs.vt.edu/corgis/datasets/json/cars/cars.json")
json_data = response.json()
#pprint(json_data)

city_mpg = []
highway_mpg = []
for record in json_data:
    if record["Fuel Information"]["Highway mpg"] <= 75:
        city_mpg.append(record["Fuel Information"]["City mpg"])
        highway_mpg.append(record["Fuel Information"]["Highway mpg"])

x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()

# plt.hist2d(city_mpg, highway_mpg)
# plt.show()

# (fig, axes) = plt.subplots(1, 2, sharey=True)
# axes[0].hist(city_mpg)
# axes[1].hist(highway_mpg)
# plt.show()

# plt.hist(city_mpg)
# plt.xlabel("City MPG")
# plt.ylabel("Frequency")
# plt.title("Distribution of City MPG in Cars Dataset")