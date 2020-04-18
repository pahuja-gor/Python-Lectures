import pprint
import requests

response = requests.get("https://data.cityofnewyork.us/api/views/25th-nujf/rows.json?accessType=DOWNLOAD")

print(response.status_code)
pprint.pprint(response.json())
