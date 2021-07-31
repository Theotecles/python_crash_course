import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # GET DATES AND HIGH AND LOW TEMPERATURES FROM THIS FILE
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%m/%d/%Y')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# PLOT THE HIGH TEMPERATURES
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.6)
ax.plot(dates, lows, c='blue', alpha=0.6)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.15)

# GET DEATH VALLEY DATA
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # GET DATES AND HIGH AND LOW TEMPERATURES FROM THIS FILE
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# ADD IT TO THE PLOT
ax.plot(dates, highs, c='red', alpha=0.3)
ax.plot(dates, lows, c='blue', alpha=0.3)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.05)

# FORMAT PLOT
ax.set_title("Daily high and temperatures - 2018 \n Sitka and Death Valley", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.ylim(10, 130)

plt.show()