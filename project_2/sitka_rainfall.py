import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    # GET THE DATES AND PRECIPITATION LEVELS
    dates, rainfalls = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%m/%d/%Y')
        try:
            rainfall = float(row[3])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            rainfalls.append(rainfall)

# PLOT THE HIGH TEMPERATURES
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, c='red')

# FORMAT PLOT
title = "Daily rainfall - 2018\n Sitka"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Rainfall (in)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()