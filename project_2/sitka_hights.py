import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # GET DATES AND HIGH TEMPERATURES FROM THIS FILE
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%m/%d/%Y')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

print(highs)

# PLOT THE HIGH TEMPERATURES
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')

# FORMAT PLOT
ax.set_title("Daily high temperatures - 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()