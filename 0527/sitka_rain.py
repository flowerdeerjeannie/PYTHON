import csv
from datetime import datetime
from pathlib import Path

from matplotlib import pyplot as plt


path = Path('/works/works_python/0527/sitka_weather_2021_full.csv')

with open(path, newline = '') as csvfile:
     reader = csv.DictReader(csvfile)


     dates, prcps = [], []
     for row in reader:
          date = datetime.strptime(row['DATE'], '%Y-%m-%d')
          dates.append(date)

          prcp = float(row['PRCP'])
          prcps.append(prcp)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, prcps, color='blue', alpha=0.5)
ax.set_title("Daily precipitation in Sitka", fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel("prcps", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()



