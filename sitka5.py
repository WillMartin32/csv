import csv
import matplotlib.pyplot as plt
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")
open_file2 = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file,delimiter=",")
csv_file2 = csv.reader(open_file2,delimiter=",")

header_row = next(csv_file)
header_row = next(csv_file2)


highs = []
dates = []
lows = []

highs2 = []
dates2 = []
lows2 = []

for row in csv_file:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    the_date = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(the_date)

for row in csv_file2:
    try:
        the_date = datetime.strptime(row[2],'%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs2.append(int(row[4]))
        lows2.append(int(row[5]))  
        dates2.append(the_date)

plt.subplot(2,1,1)
plt.plot(dates, highs,c="red")
plt.plot(dates, lows,c="blue")
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
plt.title("SITKA AIRPORT, AK US")


plt.subplot(2,1,2)
plt.plot(dates2, highs2,c="red")
plt.plot(dates2,lows2,c="blue")
plt.fill_between(dates2, highs2, lows2, facecolor='blue', alpha=0.1)
plt.title("DEATH VALLEY, CA US")


plt.suptitle("Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US")

plt.show()