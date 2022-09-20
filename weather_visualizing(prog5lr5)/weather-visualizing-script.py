import matplotlib.pyplot as pplt
import pandas
import requests
import json
from datetime import datetime


def get_weather_data(lat=33.44, lon=-94.04, api_key=None, dt=0, city='', days_range=0):
    if api_key is not None:
        result = {'city': city, 'temps': []}
        for i in range(days_range):
            req_obj = json.loads(requests.get(f'https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}'
                                              f'&lon={lon}&dt={dt}&appid={api_key}&lang=ru&units=metric').text)
            result['temps'].append([{"dt": str(measure['dt']), "temp": str(measure['temp'])} for measure in req_obj["hourly"]])
            dt += 86400
        visualise_data(json.dumps(result), days_range)
    else:
        print('API is None')


def visualise_data(json_data, days_range):
    data = pandas.read_json(json_data)
    dates = [d['dt'] for d in data['temps'][0]]
    city_name = data['city'].get(0)
    dates_hours = [datetime.utcfromtimestamp(int(i)).strftime('%H:%M') for i in dates]
    date_start = datetime.utcfromtimestamp(int(dates[0])).strftime('%d/%m/%Y')
    date_end = datetime.utcfromtimestamp(int(dates[0]) + 86400 * (days_range - 1)).strftime('%d/%m/%Y')
    all_temps = []

    pplt.figure(figsize=(15, 5))
    pplt.title(f'График температуры в городе {city_name}\nПериод: {date_start} - {date_end}')
    pplt.xlabel("Время")
    pplt.ylabel("Температура, °C")
    colors = {'g': '1 день', 'r': '2 день', 'b': '3 день', 'y': '4 день', 'm': '5 день'}
    for i in range(days_range):
        temps = [float(_t['temp']) for _t in data['temps'][i][:]]
        all_temps.append(temps)
        pplt.scatter(dates_hours, temps, c=list(colors.keys())[i], label=colors.get(list(colors.keys())[i]))
    pplt.legend(loc='lower right')
    pplt.show()

    avg_temps = [0] * len(all_temps[0])
    for i in all_temps:
        for j in range(len(i)):
            avg_temps[j] += i[j]
    for i in range(len(avg_temps)):
        avg_temps[i] /= 5

    pplt.figure(figsize=(15, 5))
    pplt.title(f'График средней температуры в городе {city_name}\nПериод: {date_start} - {date_end}')
    pplt.xlabel("Время")
    pplt.ylabel("Температура, °C")
    pplt.scatter(dates_hours, avg_temps)
    pplt.show()


if __name__ == '__main__':
    get_weather_data(55.7522, 37.6156, 'd204de47e2ed49257fc3f7cc51a8dda7', 1655164800, 'Moscow', 5)
