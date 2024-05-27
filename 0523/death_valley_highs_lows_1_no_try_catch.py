from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


path = Path('/works/works_python/0523/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    #정수로 변환하여 high,low에 저장하는 과정에서 에러가 발생하면 except 이하를 수행한다.
    #에러를 출력하고 루프로 돌아가 다음 행을 처리한다.
    except ValueError:
        print(f"missing data for {current_date}")
    #에러 없이 모든 데이터를 추출하면 else를 실행한다. 
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax1 = plt.subplots()
ax1.plot(dates, highs, color='red', alpha=0.5)
ax1.plot(dates, lows, color='blue', alpha=0.5)
ax1.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax1.set_title("Daily High and Low Temperatures, 2021\nDeath Valley, CA", fontsize=20)
ax1.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax1.set_ylabel("Temperature (F)", fontsize=16)
ax1.tick_params(labelsize=16)


plt.show()
