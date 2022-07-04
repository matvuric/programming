# Программирование
## Семестр 5

### [Лабораторная работа №1. Найти n-ю цифру последовательности из квадратов целых чисел.](https://github.com/python-basic/sem5-lr1-matvuric)
```
squareSequenceDigit(45)
>>> n = 45, result = 1
squareSequenceDigit(12)
>>> n = 12, result = 6
squareSequenceDigit(14)
>>> n = 14, result = 8
```
***
### [Лабораторная работа №2. Данные о погоде с сайта https://openweathermap.org.](https://github.com/python-basic/sem5-lr2-matvuric)
```
get_weather_data('Kiev', api_key='3943c34639f5bbda81824a4db5b51a27')
>>> {"name": "Kyiv", "coord": {"lon": 30.5167, "lat": 50.4333}, "country": "UA", "feels like": 18.28, "timezone": "UTC+3"}
```
***
### [Лабораторная работа №3. Реализация удаленного импорта.](https://replit.com/@MatviivKirill/prog5lab3#myremotemodule.py)
***
### [Лабораторная работа №4. Реализовать функцию, возвращающую ряд Фибоначчи с помощью механизма итераторов.](https://github.com/python-basic/sem3-lr4-matvuric)
```
fib(10)
>>> [0, 1, 1, 2, 3, 5, 8]
fib(1)
>>> [0, 1, 1]
fib(45)
>>> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```
***
### [Лабораторная работа №5. Визуализация погоды с помощью matplotlib.](https://github.com/matvuric/programming/tree/master/weather_visualizing)
```
get_weather_data(55.7522, 37.6156, 'd204de47e2ed49257fc3f7cc51a8dda7', 1656288000, 'Moscow', 5)
```
![](https://sun9-north.userapi.com/sun9-80/s/v1/if2/FkxEy0WBtKvsOt6Dz1jiwtsUFZf3HiK6GbygRMIubKZ_7mo_K3LIy_NcXISVd874Flk5JVCylonsLejTiUcOGZfZ.jpg?size=1500x500&quality=96&type=album)
![](https://sun9-north.userapi.com/sun9-77/s/v1/if2/xAwOvnAJY2y93FEZwMAUy8bkVCvSfjbEl0yFCPQ2WFhIfKkPSbWkFUPoEckUj1iHMNX7hhU8JkOmTHKCCPLigEL-.jpg?size=1500x500&quality=96&type=album)
***
### [Лабораторная работа №6. Реализация паттерна Singleton к функции получения валют.](https://github.com/matvuric/programming/tree/master/singleton)
```
print(CurrenciesList().get_currencies(["R01090B", "R01720", "R01565"]))
>>> {'R01090B': ('20,9514', 'Белорусский рубль'), 'R01565': ('11,8839', 'Польский злотый'), 'R01720': ('18,2867', 'Украинских гривен')}
```
***
### [Лабораторная работа №7. Реализация паттерна Decorator к функции получения валют.](https://github.com/matvuric/programming/tree/master/decorator)
```
show_currencies(wrapped_cur_list_json)
show_currencies(wrapped_cur_list_csv)
show_currencies(wrapped_cur_list)
>>> {
      "R01035": [
      ...
      "R01815": [
        "41,4458",
        "Вон Республики Корея"
      ]
    }
```
***
### [Лабораторная работа №9. Визуализация курсов валют.](https://colab.research.google.com/drive/1BbstCcPGewLtIWguivoYQzRfA6yLmOCv?usp=sharing)
```
viz_currencies()
viz_dollar()
```
![](https://sun9-east.userapi.com/sun9-29/s/v1/if2/or8WfTwQsbOL91UWXEbE2vPtyRjMcOqFS1RDfxHMN4oi-ZF03WGADcUfR6Wv2ZJ8n8munwhnwAxNw-XAR21a02CU.jpg?size=1200x800&quality=96&type=album)
***

## Семестр 6
### [Лабораторная работа №1-2. Статистика по файлам Retail.csv и MarketingSpend.csv](https://replit.com/@MatviivKirill/prog6lab1#main.py)
```
print("Среднее: ", data2.get_mean)
>>> Среднее:  (2843.5616438356165, 1905.8807397260264)
print("Максимум: ", data2.max)
>>> Максимум:  (5000.0, 4556.93)    
print("Минимум: ", data2.min)
>>> Минимум:  (500.0, 320.25) 
print("Дисперсия: ", data2.disp)
>>> Дисперсия:  (904376.3557890786, 1531702.423118352)
print("Среднее квадратичное отклонение: ", data2.sigma_sq)
>>> Среднее квадратичное отклонение:  (950.9870429133505, 1237.6196601211343)
```
***
### [Лабораторная работа №3-4. Статистика по Титанику](https://replit.com/@MatviivKirill/prog6lab2#main.py)
```
get_sex_distrib(data)
>>> (577, 314)
...
find_popular_adult_names(data)
>>> ('William', 'Anna')
```
***
### [Лабораторная работа №5. Решение задачи регрессии по статистике посещений веб-сервера компании.](https://replit.com/@MatviivKirill/prog6lab5#main.py)
```
clrs = {1: 'k', 2: 'b', 3: 'g', 5: 'm', 10: 'c', 20: 'r'}
for i in clrs:
  pol(i, clrs.get(i))
>>> MSE1 4.3182e+05
    MSE1 (для данных ДО 3.5 недели)= 1.8845e+05
    MSE1 (для данных c 3.5 недели по 4.1 недели)= 1.2355e+05
    MSE1 (только для данных с 4.1 недели)= 2.4832e+05
    ...
```
![](https://sun9-west.userapi.com/sun9-51/s/v1/if2/MciTbrw3ywJWWQXqc9Ecp4lqVujEKuvUW1Mi-HoltzpuCIa_qq-Gnyc27Q_4sGUdWl3RxbATWgN5ue2CZD-J7oTb.jpg?size=640x480&quality=96&type=album)
***
### [Лабораторная работа №6. Решение задачи регрессии по данным о ценах на недвижимость.](https://colab.research.google.com/drive/1xQOf-rtTKB2dqY278Ubwzh1zj6nJM1EA)
