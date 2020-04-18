location = {
    "city":"Blacksburg",
    "state":"VA",
    "zip":24060
}

current_weather = {
    "temperature":60,
    "humidity":90,
    "wind":2
}

time = {
    "hour":12,
    "minute":34,
    "second":15
}

date = {
    "month":"October",
    "day":28,
    "year":2019,
    "time":time
}

weather_record = {
    "location":location,
    "forecast":current_weather,
    "datetime":date
}

###################3

location2 = {
    "city":"Christiansburg",
    "state":"VA",
    "zip":24060
}

current_weather2 = {
    "temperature":90,
    "humidity":75,
    "wind":5
}

time2 = {
    "hour":12,
    "minute":34,
    "second":15
}

date2 = {
    "month":"July",
    "day":28,
    "year":2017,
    "time":time2
}

weather_record2 = {
    "location":location2,
    "forecast":current_weather2,
    "datetime":date2
}

list_of_weather = []
list_of_weather.append(weather_record)
list_of_weather.append(weather_record2)

def average_temperature(all_records):
    count = 0
    total = 0
    for record in all_records:
        forecast = record["forecast"]
        temperature = forecast["temperature"]
        count = count + 1
        total = total + temperature
    return total / count

print("Average Temperature: " + str(average_temperature(list_of_weather)))

def populate_record():
    location = input("What is the location? ")
    split_location = location.split(",")
    city = split_location[0]
    state = split_location[1]
    zipcode = int(split_location[2])
    location_dictionary = {
        "city":city,
        "state":state,
        "zip":zipcode
    }

    forecast_dictionary = {
        "temperature": int(input("What is the current temperature? ")),
        "humidity": int(input("What is the current humidity? ")),
        "wind": int(input("What is the current wind speed? "))
    }

    datetime_dictionary = {
        "month":"November",
        "day":1,
        "year":3000,
        "time": {
            "hour":20,
            "minute":00,
            "second":00
        }
    }

    return {
        "location":location_dictionary,
        "forecast":forecast_dictionary,
        "datetime":datetime_dictionary
    }

list_of_weather.append(populate_record())
print("New Average Temperature: " + str(average_temperature(list_of_weather)))