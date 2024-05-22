from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt
import os
print(os.getcwd())

path = Path('/works/works_python/0522/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()
# lines는 파일의 각 줄을 요소로 가진 리스트, [ 안에 '"STATION","NAME","DATE","TAVG","TMAX","TMIN"', '"USW00025333","SITKA AIRPORT, AK US","2021-01-01",,"44","40", 로 각 줄이 다 담겨져있음 ]

reader = csv.reader(lines)
#각 줄 요소를 읽어가지고 하나를 reader에 할당함. '"STATION","NAME","DATE","TAVG","TMAX","TMIN' 이거 하나가 reader라고
header_row = next(reader) 
#next(reader)를 호출하여 첫 번째 줄을 읽어

# Extract dates and high temperatures.
dates, highs = [], []
for row in reader: # row : row0-"USW00025333",row1-"SITKA AIRPORT, AK US",row2-"2021-01-01",,row3-"44",row4-"40"
    current_date = datetime.strptime(row[2], '%Y-%m-%d') 
    #datetime.strptime() 함수는 문자열을 날짜와 시간 객체로 변환하는 파이썬의 메서드
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)
#csv에서 리스트화 해서 제일 윗줄을 읽어내 주고,(직접적으로 활용은 안하지만) CSV 파일의 첫 번째 줄은 종종 열에 대한 설명이 포함되어 있으므로
#읽어내주어야 데이터 처리 및 분석 가능함. 
#x.y축으로 활용할 거를 빈 배열로 만들어 놓고  for문 돌린다. 
#reader로 바꾼거를 하나하나 읽어내면서 필요한거를 가져와서 x.y 배열을 채워가지고 그래프를 만든다. 

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')

# Format plot.
ax.set_title("Daily High Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
