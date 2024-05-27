from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt


path = Path('/works/works_python/0522/sitka_weather_2021_simple.csv')
#파일 내용 읽기. 각 줄을 요소로 하는 리스트.
lines = path.read_text().splitlines()

#reader는 한 줄이 아니고 각 줄이 "" 로 되어있는걸 [] 리스트화 하여 [],[],[],[]로 출력할 수 있는 반복자임
#직접적으로 reader를 출력할 수는 없기 때문에 밑에서 for문을 돌려서 [] 하나가 row 인거지 
reader = csv.reader(lines)

#header_row는 CSV 파일의 첫 번째 줄을 나타내며, 열의 이름을 포함
header_row = next(reader) 


#x.y축으로 활용할 거를 빈 배열로 만들어 놓고  for문 돌린다. 
#reader로 바꾼거를 하나하나 읽어내면서 필요한거를 가져와서 x.y 배열을 채워가지고 그래프를 만든다. 
dates, highs, lows, avgs = [], [], [], []
for row in reader: # row : row0-"USW00025333",row1-"SITKA AIRPORT, AK US",row2-"2021-01-01",,row3-"44",row4-"40"
    current_date = datetime.strptime(row[2], '%Y-%m-%d') 
    #datetime.strptime() 함수는 문자열을 날짜와 시간 객체로 변환하는 파이썬의 메서드
    try:
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"missing value={row}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)



# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax2 = plt.subplots()
ax2.plot(dates, highs, color='green', alpha=0.5)
ax2.plot(dates, lows, color='orange', alpha=0.5)
ax2.fill_between(dates, highs, lows, facecolor = 'black', alpha=0.1)
# Format plot.
ax2.set_title("Daily High Temperatures, 2021", fontsize=24)
ax2.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax2.set_ylabel("Temperature (F)", fontsize=16)
ax2.tick_params(labelsize=16)


plt.show()
